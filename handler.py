# import image
# import mouse
import profile
import skill
import os  # Used to check if a file is empty
import random  # Used for random number generation
import fileinput  # Used for overwriting single lines in files
from fnmatch import fnmatch, fnmatchcase  # Used for wildcard searches in strings

# -----Helper Functions-----
# Creates and returns a default Profile object
def default_profile():
    skill_map = default_skill_map()
    return profile.Profile('default', '', '', skill_map, '3')

# Returns a map which contains a string key for each Runescape classic skill, values are Skill objects
def default_skill_map():
    skill_list = ['ATTACK', 'COOKING', 'CRAFTING', 'DEFENCE', 'FIREMAKING', 'FISHING','HITPOINTS','MAGIC',
                  'MINING', 'PRAYER', 'RANGED', 'RUNECRAFTING','SMITHING','STRENGTH','WOODCUTTING']
    default_active_status = 1  # Set to True, but if it's a bool it won't print as a number when cast as a string
    default_level = 1
    default_priority = 99
    skill_map = {}
    for sk in skill_list:
        skill_map[sk] = skill.Skill(default_active_status, sk, default_priority, default_level)
    return skill_map

# Checks if a file exists, must be passed the full file name
def file_exists(file_name, dir_path):
    for file in os.listdir(dir_path):
        if file == file_name:
            return True
    return False

# Returns a boolean of whether a file is empty
def file_is_empty(file_path):
    return os.stat(file_path).st_size == 0

def file_rename(file_name, name):
    file_path = './profiles/' + make_txt_file_name(file_name)
    new_name = './profiles/' + make_txt_file_name(name)
    os.rename(file_path, new_name)
    return False

# Writes to a file at all lines matching the line_name
def file_write(file_name, line_name, value):
    file_path = './profiles/' + file_name
    for line in fileinput.input(file_path, inplace=True):
        if fnmatch(line, line_name + '*'):
            item = line.split('=')
            index = 0
            if len(item) > 1:  # Count the number of characters to remove from the line
                for i in range(0, len(item[1])):
                    index -= 1
            print(line.replace(line.rstrip(), line[:index] + value), end='')
        else:
            print(line, end='')
    return False

# Perform initial setup as dictated by the init file
# Returns tuple, [Success boolean, active profile].
# FIXME - How to make it so the exact init lines that failed can be returned to main for error-checking?
# FIXME - If no intialization.txt file is found, it should be generated with default info.
# FIXME - Refactor to return dict, {'Success': success, 'Value': value}
def initialization(file_name, dir_path):
    if not file_exists(file_name, dir_path):  # If no init file exists, return false and default profile
        return (False, default_profile())
    file_path = dir_path + file_name
    with open(file_path) as f:  # Open the init file
        lines = f.read().splitlines()
        for line in lines:
            item = line.split('=')
            if item[0] == 'DEFAULT_PROFILE':  # Set a default profile as the active one
                if(len(line) < 2 or item[1] == ''):
                    return (False, default_profile())
                path = './profiles/' + item[1]
                (load_success, loaded_profile) = map_read_profile(path)
                if load_success:
                    return (True, loaded_profile)
                else:
                    return (True, default_profile())
    return (False, default_profile())                

# Returns whether the profile is set as the default in initialization.txt
def is_default_profile(profile_name):
    profile_file_name = make_txt_file_name(profile_name)  # Ensure this only deals with txt file names
    with open('initialization.txt', 'r') as f:  # Find the name of the default profile
        lines = f.read().splitlines()
        old_profile_name = ''
        for i in range(0, len(lines)):
            item = lines[i].split('=')
            if item[0] == 'DEFAULT_PROFILE':
                if len(item) > 1:
                    old_profile_name = item[1]
                i = len(lines)  # Exit the loop
        if old_profile_name == profile_file_name:
            return True
    return False

def load(profile_name):
    file_name = make_txt_file_name(profile_name)  # Ensure this handles file names
    file_path = './profiles/' + file_name
    if file_exists(file_name, './profiles/'):
        result = map_read_profile(file_path)
        if result[0]:
            loaded_profile = result[1]
            return True, loaded_profile
    print('Error: Failed to load profile \'' + file_name + '\'.')
    return False, None

# Converts a string to have a .txt extension (for use with profile name that may or may not have extensions)
def make_txt_file_name(profile_name):
    if profile_name.endswith('.txt'):
        return profile_name
    else:
        return profile_name + '.txt'

# Reads the content from a profile file and returns a Profile object
def map_read_profile(file_path):
    skill_dict = {}
    username = ''
    profile_name = ''
    password = ''
    skill_name = ''  # FIXME - Is this needed, should it be incorporated below?
    combat_level = ''
    with open(file_path) as f:
        lines = f.read().splitlines()
        for line in lines:
            split = line.split('=')
            identifier = split[0]
            value = split[1]
            if identifier == 'NAME':
                profile_name = value
            elif identifier == 'USERNAME':
                username = value
            elif identifier == 'PASSWORD':
                password = value
            elif identifier == 'COMBAT_LEVEL':
                combat_level = value
            elif '_ACTIVE' in identifier:
                active_split = identifier.split('_')
                dict_identifier = active_split[0]
                if dict_identifier in skill_dict:
                    skill_dict[dict_identifier].active = value
                else:
                    sk = skill.Skill(1, dict_identifier, value, 0)
                    skill_dict[dict_identifier] = sk
            elif '_PRIO' in identifier:
                prio_split = identifier.split('_')
                dict_identifier = prio_split[0]
                if dict_identifier in skill_dict:
                    skill_dict[dict_identifier].priority = value
                else:
                    sk = skill.Skill(dict_identifier, value, 0)
                    skill_dict[dict_identifier] = sk
            elif '_PRIO' not in identifier and '_ACTIVE' not in identifier:  # Handles plain skill names
                if identifier in skill_dict:
                    skill_dict[identifier].level = value
                else:
                    sk = skill.Skill(1, identifier, 0, value)
                    skill_dict[identifier] = sk
            else:
                return False, None
    loaded_profile = profile.Profile(profile_name, username, password, skill_dict, combat_level)
    return True, loaded_profile

# FIXME - This needs a better name, but I don't know what to call it
# Creates a new profile file
def new_profile_file(profile):
    file_name = profile.get_name() + '.txt'
    dir_path = './profiles/'
    if file_exists(file_name, dir_path):  # Check the file doesn't already exist
        return False
    with open('profiles/' + profile.name + '.txt', 'w+') as f:
        f.write('NAME=' +                   profile.name +
                '\nUSERNAME=' +             profile.get_username() +
                '\nPASSWORD=' +             profile.get_password() +
                '\nCOMBAT_LEVEL=' +         str(profile.get_combat_level()) +
                skill_dict_output_string(profile.skill_dict)
                )
        return True

# Returns a list of all the arguments passed
def parse_args(input_list):
    arg_list = [None] * (len(input_list) - 1)  # Init an empty list equal to the number of the arguments being passed
    for i in range(0, len(input_list) - 1):
        arg_list[i] = input_list[i + 1]
    return arg_list

# Prompts the user (y/n) if they want to perform a certain action on a certain named thing
def prompt_yn(action_name, name):
    while True:
        user_input = input('This action cannot be undone, are you sure you want to ' +
                           action_name + ' \'' + name + '\'(y/n)? ').upper()
        if user_input == 'Y':
            return True
        elif user_input == 'N':
            return False

# Returns a random, valid priority (an integer in the range 0 to 99)
def random_priority():
    return random.randint(0, 99)

# Returns a printable string for a given skill dictionary
def skill_dict_output_string(skill_dict):
    string = ''
    for name, sk in sorted(skill_dict.items()):
        string += '\n'+name+ '='+ str(sk.level)
        string += '\n'+name+'_ACTIVE='+str(sk.active)
        string += '\n'+name+'_PRIO='+ str(sk.priority)
    return string


# -----Functions for Commands-----
def auto():  # Allows the system to take control, deciding the best course of action for the character
    return False
    # Create and populate a list of objectives based on user-set goals via the commandline
    # Then either select one at random (to avoid detection) or create an optimal path between the tasks

# Creates a fresh profile with the passed in name, username, and (optionally) password
def create(input_list):
    arg_list = parse_args(input_list)
    if len(arg_list) < 2:
        print('Error: Too few arguments. Pass the profile_name and username after the command.')
        return False
    elif file_exists(make_txt_file_name(arg_list[0]), './profiles/'):
        print('Error: Profile already exists. Try updating or deleting it instead.')
        return False
    else:
        new_profile = default_profile()  # Init to the default profile
        for i in range(0, len(arg_list)):  # Assign the passed in values to the profile
            if i == 0:
                new_profile.set_name(arg_list[i])
            elif i == 1:
                new_profile.set_username(arg_list[i])
            elif i == 2:
                new_profile.set_password(arg_list[i])
        if not new_profile_file(new_profile):
            print('Error: File already exists. Try deleting the old profile before creating it again.')
            return False
        return True

# FIXME - Is it necessary to reset the default_profile to default.txt after deletion?
# Deletes a profile file based on a passed in profile name
def delete(input_list):
    arg_list = parse_args(input_list)
    file_name = make_txt_file_name(arg_list[0])
    if file_exists(file_name, './profiles/'):
        new_default_file_name = ''
        if is_default_profile(file_name):  # Handle resetting default profile if it's being deleted
            if not file_name == 'default.txt':  # If deleting default.txt, set DEFAULT_PROFILE to the empty string
                new_default_file_name = 'default.txt'  # Otherwise, set the default profile to default.txt
            for line in fileinput.input('initialization.txt', inplace=True):
                if fnmatch(line, 'DEFAULT_PROFILE=*'):
                    print(line.replace(line, 'DEFAULT_PROFILE=' + new_default_file_name), end='')
                else:
                    print(line, end='')
        if prompt_yn('delete', file_name):
            file_path = './profiles/' + file_name
            os.remove(file_path)  # Perform the delete
            return True
        else:
            return False
    print('Error: Profile \'' + file_name + '\' not found.')
    return False

# FIXME - Many commands remain without explanations, fill them in or delete them as development progresses
def help_command(input_list):
    arg_list = parse_args(input_list)
    if len(arg_list) > 0:
        arg_list[0] = arg_list[0].upper()  # Uppercase the command for easy recognition
    if len(arg_list) < 1:  # If no arguments, then print general help
        print('AUTO\t\tAllows the system to automatically create objectives and work to complete them\n'
              'CREATE\t\tTakes two arguments (profile_name, username) to create a profile with that character\'s data\n'
              'DELETE\t\tTakes one argument (profile_name) and deletes the profile from the system'
              'HELP\t\tProvides a helpful list of the commands and how to use them\n'
              'LOAD\t\tTakes one argument (profile_name) and loads that profile\n'
              'LOGIN\t\tTakes two arguments (username, password) and logs in the user\n'
              'PRINT\t\tTakes one argument (profile_name) and prints its contents.\n'
              'PRIORITY\tTakes a list of skills and priorities\n'
              'RANDOMIZE\tTakes an optional parameter of profile name to have its priorities randomized.\n'
              'RESETPRIO\tTakes an optional parameter of profile name to have its priorities reset to 99.\n'
              'START\t\tStarts the bot, allowing it to create its own path to objectives based on its profile.\n'
              'SETDEFAULT\tTakes one argument (profile_name) to set a profile as the default one loaded on launch\n'
              'STOP\t\tHalts all automation and allows the user full control of the bots\n'
              'QUIT\t\tExits this program')
    elif arg_list[0] == 'AUTO':
        print('Allows the program to automatically create objectives based on the active profile\'s priorities ' +
              'and skill levels and then works to complete those objectives.')
    elif arg_list[0] == 'CREATE':
        print('Takes two arguments for profile name and username, and a third (optional) parameter for password. '
              'It populates the profile with data from the corresponding RS character\'s skills.\n' +
              '\tCREATE <PROFILENAME> <USERNAME> - Creates a profile associated with the username\n' +
              '\tCREATE <PROFILENAME> <USERNAME> <PASSWORD> - Same as above but also stores a password in the profile')
    elif arg_list[0] == 'DELETE':
        print('DELETE...')
    elif arg_list[0] == 'HELP':
        print('Provides information about available commands, what they do and how to use them\n'
              '\tHELP <COMMAND_NAME> - Provides a more detailed explanation on the passed in command')
    elif arg_list[0] == 'LOAD':
        print('Takes one argument for profile name and loads that into the active profile so that other commands ' +
              'can use those settings.\n'
              '\tLOAD <PROFILENAME> - Loads the profile with the specified name as the active profile')
    elif arg_list[0] == 'LOGIN':
        print('LOGIN...')
    elif arg_list[0] == 'PRINT':
        print('Takes one optional argument for the profile name. If no argument is passed to it, then it loads the ' +
              'active profile.\nBoth profile names and file names(with extensions) are valid.\n'
              '\tPRINT - Prints the currently loaded profile\n' +
              '\tPRINT <PROFILENAME> - Prints the profile with the passed in name if it exists')
    elif arg_list[0] == 'PRIORITY':
        print('\tPRIORITY...')
    elif arg_list[0] == 'RANDOMIZE':
        print('\tRANDOMIZE...')
    elif arg_list[0] == 'RESETPRIO':
        print('\tRESETPRIO...')
    elif arg_list[0] == 'SETDEFAULT':
        print('Takes one argument of profile name to be set as the new default profile loaded on launch. ' +
              'Both profile names and file names(with \'.txt\' extensions) are valid.\n' +
              '\tSETDEFAULT <PROFILENAME> - Sets the default profile to be the new profile loaded at launch\n')
    elif arg_list[0] == 'STOP':
        print('\tSTOP...')
    elif arg_list[0] == 'QUIT':
        print('Takes no arguments. It is used to exit the program.\n' +
              '\tQUIT - Stops all execution of the program and exits')
    else:
        print('Help doesn\'t recognize this command. Try typing \'HELP\' to see a list of valid commands.')

# Load the profile with the passed in name, returns a Tuple of (Boolean, Profile)
def load_command(input_list):
    arg_list = parse_args(input_list)
    if len(arg_list) < 1:
        print('No profile name entered.')
        return False, None
    result = load(arg_list[0])
    if result[0]:
        loaded_profile = result[1]
        return True, loaded_profile
    return False, None

# FIXME - Take an optional parameter for world number
def login(input_list):
    # Want to log in the user with command line arguments, then wait for more input from the user
    # login(user, pass) and maybe an optional third parameter for world number
    return False

# FIXME - Initialize priorities to values that follow a hardcoded "optimal" route based on testing/timing routes
# FIXME - Looking back at this, I'm not sure what it should do, this might just be consolidated into AUTO later
def optimize():
    return False

# FIXME - If an empty file is loaded and then attempted to print, this fails, because it tries to fetch profile.name()
# FIXME     which doesn't exist in the emtpy file. Is there a way to fetch the file's name and use that in order to
# FIXME     give a more helpful error?
# FIXME - This actually reads the active profile's contents from a file, rather than using the object in main
# FIXME     this is a small, subtle difference, but it could affect performance later and maybe create some unusual
# FIXME     behavior in the program now.
# Prints the contents of a file to the console, or those of the active profile if no arguments are passed
def print_command(input_list, profile):
    arg_list = parse_args(input_list)
    if len(arg_list) < 1:  # If no arg passed to PRINT, it uses the active profile
        file_name = make_txt_file_name(profile.get_name())
        dir_path = './profiles/'
        if file_exists(file_name, dir_path):
            file_path = dir_path + file_name
            with open(file_path) as f:
                line = f.read().splitlines()
                for i in range(0, len(line)):
                    print(line[i])
            return True
        else:
            print('Error: Active profile failed to load. Try reloading it and then printing again.')
    else:
        file_name = make_txt_file_name(arg_list[0])
        dir_path = './profiles/'
        if file_exists(file_name, dir_path):
            file_path = dir_path + file_name
            with open(file_path) as f:
                line = f.read().splitlines()
                for i in range(0, len(line)):
                    print(line[i])
            return True
        else:
            print('Error: Profile not found. Check that file exists and it\'s spelled correctly.')
    return False

# This sets the priority of various skills to passed in values
# FIXME - I think this needs a new name and envisioned functionality, passing so many arguments seems poorly designed
def priority(input_list):
    # Have this take a list of <skill, prio, skill, prio, skill, prio...> and optionally a character name?
    # This will open the file for the profile, then find the skills that match its args and assign the new priority
    return False

# Note: Takes a single parameter for profile name and randomizes its priorities. No args means it uses active profile
def randomize(input_list, profile):
    arg_list = parse_args(input_list)
    active_profile = profile  # Init with the active profile
    if len(arg_list) > 0:  # If user passed a profile name, use it
        result = load(arg_list[0])
        if result[0]:  # On a successful load
            active_profile = result[1]
        else:
            print('Error: Failed to load passed in profile.')
    file_name = make_txt_file_name(active_profile.get_name())
    if not prompt_yn('randomize', file_name):
        return False
    file_path = './profiles/' + file_name
    for line in fileinput.input(file_path, inplace=True): # Perform the randomization
        if fnmatch(line, '*PRIO=*'):  # Check if the line relates to priority
            item = line.split('=')
            index = 0
            if len(item) > 1:  # Count the number of characters to remove from the end of the line
                for i in range(0, len(item[1])):
                    index -= 1
            print(line.replace(line.rstrip(), line[:index] + str(random_priority())), end='')
        else:
            print(line, end='')
    return False

# FIXME - Place this under helpers alphabetically
# FIXME - How to do randomized values in a general 'all prios' function?
# FIXME     Maybe make a sub function for updating an individual prio and have this call that?
# FIXME - I really want to avoid having to loop through the file more than once to change all its priorities
# FIXME     which would be very easy to do, because of how file writing has to occur. You can't just replace a single
# FIXME     line, you have to copy the whole file to change a single line, so you want to lump changes together.
# FIXME - This is incomplete, don't use it yet.
# Takes two parameters, profile name to be changed, and value of the priorities to be reset to
def update_all_priorities(profile_name, new_value):
    file_name = make_txt_file_name(profile_name)
    file_path = './profiles/' + file_name
    for line in fileinput.input(file_path, inplace=True):  # Perform change
        if fnmatch(line, '*PRIO=*'):  # Check if the line relates to priority
            item = line.split('=')
            index = 0
            if len(item) > 1:  # Count the number of characters to remove from the end of the line
                for i in range(0, len(item[1])):
                    index -= 1
            print(line.replace(line.rstrip(), line[:index] + '99'), end='')
        else:
            print(line, end='')
    return False

# FIXME - Consider putting replacing priorities into its own helper, this uses the functionality twice and randomize uses it once
# Note: This takes a single (optional) argument of profile name (or file name) and resets the priorities all to 99.
def resetpriority(input_list, active_profile):
    arg_list = parse_args(input_list)
    if len(arg_list) < 1:  # Use the active profile
        file_name = make_txt_file_name(active_profile.get_name())
        if prompt_yn('reset', file_name):
            file_path = './profiles/' + file_name
            for line in fileinput.input(file_path, inplace=True):  # Perform the reset
                if fnmatch(line, '*PRIO=*'):  # Check if the line relates to priority
                    item = line.split('=')
                    index = 0
                    if len(item) > 1:  # Count the number of characters to remove from the end of the line
                        for i in range(0, len(item[1])):
                            index -= 1
                    print(line.replace(line.rstrip(), line[:index] + '99'), end='')
                else:
                    print(line, end='')
            # FIXME - This needs to reload the current profile with the new load(), right now the active_profile is returned unchanged
            return True, active_profile
    else:  # Fetch the passed in profile (if it exists)
        file_name = make_txt_file_name(arg_list[0])
        if not file_exists(file_name, './profiles/'):
            return False, None
        if prompt_yn('reset', file_name):
            file_path = './profiles/' + file_name
            for line in fileinput.input(file_path, inplace=True):  # Perform the reset
                if fnmatch(line, '*PRIO=*'):  # Check if the line relates to priority
                    item = line.split('=')
                    index = 0
                    if len(item) > 1:  # Count the number of characters to remove from the end of the line
                        for i in range(0, len(item[1])):
                            index -= 1
                    print(line.replace(line.rstrip(), line[:index] + '99'), end='')
                else:
                    print(line, end='')
            # FIXME - This needs to reload the current profile with the new load(), right now the active_profile is returned unchanged
            return True, active_profile
        return False, None

# Takes a single argument of profile_name and sets that profile as the default
def setdefault(input_list):
    arg_list = parse_args(input_list)
    if len(arg_list) < 1:
        print('Error: No profile name passed.')
        return False
    file_name = make_txt_file_name(arg_list[0])
    if file_exists(file_name, './profiles/'):
        with open('initialization.txt', 'r+') as f:  # Find the name of the old profile
            lines = f.read().splitlines()
            old_profile = ''
            for i in range(0, len(lines)):
                item = lines[i].split('=')
                if item[0] == 'DEFAULT_PROFILE':
                    if len(item) > 1:
                        old_profile = item[1]
                    i = len(lines)  # Exit the loop
        for line in fileinput.input('initialization.txt', inplace=True):
            # The comma prevents line breaks, and the end='' prevents a newline character
            print(line.replace('DEFAULT_PROFILE=' + old_profile, 'DEFAULT_PROFILE=' + file_name), end='')
        return True
    else:
        print('Error: Profile not found.')
    return False

# Used to set various fields in profiles
def setusername(input_list, active_profile):
    arg_list = parse_args(input_list)
    if len(arg_list) < 1:
        print('Error: No username parameter specified.')
        return False, None
    result = load(active_profile.get_name())
    if not result[0]:
        # FIXME - This should pass the error from load() to main.py
        return False, None
    active_profile.set_username(arg_list[0])
    file_name = make_txt_file_name(active_profile.get_name())
    file_write(file_name, 'USERNAME=', arg_list[0])
    # FIXME - Check if this name is used in initialization.txt - reseting initialization.txt should be a helper

    return True, active_profile

# Takes no parameters. It starts the bot, creating a path between hotspots based on the active profile's settings
# It should mainly consider priority, proximity, and whether some skills are set as 'active' (to be implemented)
# FIXME - Should this take a profile name as a parameter? It seems like overkill, why even load profiles, then?
def start():
    return False

# FIXME - Want to be able to pause all operations and allow user to manually control their computer
def stop():
    return False
