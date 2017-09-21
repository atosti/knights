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

# Checks if a file exists, must be passed the full file name
def file_exists(file_name, dir_path):
    for file in os.listdir(dir_path):
        if file.startswith(file_name) and file.endswith(file_name):  # FIXME - More optimal way to do this?
            return True
    return False

# Returns a boolean of whether a file is empty
def file_is_empty(file_path):
    return os.stat(file_path).st_size == 0

# Converts a string to have a .txt extension (for use with profile name that may or may not have extensions)
def make_txt_file_name(profile_name):
    file_name = profile_name
    if not is_txt_file(file_name):
        file_name += '.txt'
    return file_name

# Perform initial setup as dictated by the init file
# FIXME - How to make it so the exact init lines that failed can be returned to main for error-checking?
# FIXME - If no intialization.txt file is found, it should be generated with default info.
def initialization(file_name, dir_path):
    result_0 = False
    result_1 = None
    total_result = (result_0, result_1)  # Must contain an element for each object to be returned
    if not file_exists(file_name, dir_path):  # If no init file exists, return false and default profile
        result_1 = default_profile()
        total_result = (result_0, result_1)
        return total_result
    file_path = dir_path + file_name
    with open(file_path) as f:  # Open the init file
        lines = f.read().splitlines()
        success = []  # A list of whether a each line succeeded
        for i in range(0, len(lines)):
            item = lines[i].split('=')
            if item[0] == 'DEFAULT_PROFILE':  # Set a default profile as the active one
                if len(item) < 2:  # Check there's a value to the right of the equals sign
                    result_1 = default_profile()
                    success.append(False)
                elif file_exists(item[1], './profiles/'):
                    path = './profiles/' + item[1]
                    result = map_read_profile(path)
                    if result[0]:  # If the profile read succeeds
                        result_1 = result[1]
                        success.append(True)
                    else:
                        result_1 = default_profile()
                        success.append(False)
        result_0 = True  # Initialize to True, then check validity of each success item
        for i in range(0, len(success)):  # Determine whether to return True or False
            if not success[i]:
                result_0 = False
                i = len(lines)  # Exit loop on first False found
    total_result = (result_0, result_1)  # [Success boolean, active profile]
    return total_result

# Returns a boolean of whether a .txt file name was passed to it
def is_txt_file(name):
    if name.endswith('.txt'):
        return True
    return False

# Reads the content from a profile file and returns a Profile object
def map_read_profile(file_path):
    skill_dict = {}
    username = ''
    profile_name = ''
    password = ''
    skill_name = ''
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
            elif '_PRIO' not in identifier:
                if identifier in skill_dict:
                    skill_dict[identifier].level = value
                else:
                    sk = skill.Skill(identifier, 0, value)
                    skill_dict[identifier] = sk
            elif '_PRIO' in identifier:
                prio_split = identifier.split('_')
                dict_identifier = prio_split[0]
                if dict_identifier in skill_dict:
                    skill_dict[dict_identifier].priority = value
                else:
                    sk = skill.Skill(dict_identifier, value, 0)
                    skill_dict[dict_identifier] = sk
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

# Returns a random, valid priority (an integer in the range 0 to 99)
def random_priority():
    return random.randint(0, 99)

# Returns a printable string for a given skill dictionary
def skill_dict_output_string(skill_dict):
    string = ''
    for name, sk in sorted(skill_dict.items()):
        string += '\n'+name+ '='+ str(sk.level)
        string += '\n'+name+'_PRIO='+ str(sk.priority)
    return string

# Returns a map which contains a string key for each Runescape classic skill, values are Skill objects
def default_skill_map():
    skill_list = ['ATTACK', 'COOKING', 'CRAFTING', 'DEFENCE', 'FIREMAKING', 'FISHING','HITPOINTS','MAGIC',
    'MINING', 'PRAYER', 'RANGED', 'RUNECRAFTING','SMITHING','STRENGTH','WOODCUTTING']
    default_priority = 99
    default_level = 1
    skill_map = {}
    for sk in skill_list:
        skill_map[sk] = skill.Skill(sk, default_priority, default_level)
    return skill_map


# -----Functions for Commands-----
def auto():  # Allows the system to take control, deciding the best course of action for the character
    return False
    # Create and populate a list of objectives based on user-set goals via the commandline
    # Then either select one at random (to avoid detection) or create an optimal path between the tasks

def create(input_list):
    arg_list = parse_args(input_list)
    if len(arg_list) < 2:
        print('Error: Too few arguments. Pass the profile_name and username after the command.')
        return False
    elif file_exists(make_txt_file_name(arg_list[0]), './profiles/'):
        print('Error: Profile already exists. Try updating or deleting it instead.')
        return False
    else:
        profile_name = ''
        username = ''
        password = ''
        for i in range(0, len(arg_list)):
            if i == 0:
                profile_name = arg_list[i]
            elif i == 1:
                username = arg_list[i]
            elif i == 2:
                password = arg_list[i]
        skill_map = default_skill_map();  # FIXME - Instead of defaulting skills, implement fetching based on username
        new_profile = profile.Profile(profile_name, username, password,skill_map, 3)
        if not new_profile_file(new_profile):
            print('Error: File already exists. Try deleting the old profile before creating it again.')
            return False
        return True

# FIXME - Check if the deleted profile is the default, if so reset the default profile in initialization.txt
# FIXME - The check for y/n from the user should be put into a helper function
# FIXME     'This action cannot be undone do you want to <action_name> \'<file_name>\' (y/n)?'
# FIXME     and put it into a loop checking if the user press Y or N
def delete(input_list):
    arg_list = parse_args(input_list)
    file_name = make_txt_file_name(arg_list[0])
    if file_exists(file_name, './profiles/'):
        while True:
            user_input = input(
                'This action cannot be undone, do you want to delete \'' + file_name + '\'(y/n)? ').upper()
            if user_input == 'Y':
                file_path = './profiles/' + file_name
                os.remove(file_path)  # Perform the delete
                return True
            elif user_input == 'N':
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
              'RESET\t\tTakes an optional parameter of profile name to have its priorities reset to 99.\n'
              'START\t\tStarts the bot, allowing it to create its own path to objectives based on its profile.\n'
              'SETDEFAULT\tTakes one argument (profile_name) to set a profile as the default one loaded on launch\n'
              'STOP\t\tHalts all automation and allows the user full control of the bots\n'
              'QUIT\t\tExits this program')
    elif arg_list[0] == 'AUTO':
        print('Allows the program to automatically create objectives based on the active profile\'s priorities ' +
              'and skill levels and then works to complete those objectives.')
    elif arg_list[0] == 'CREATE':
        print('Requires two arguments for profile name, username, and an optional third parameter for password. It ' +
              'populates the profile with data from the corresponding RS character\'s skills.\n' +
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
        print('PRIORITY...')
    elif arg_list[0] == 'RANDOMIZE':
        print('RANDOMIZE...')
    elif arg_list[0] == 'RESET':
        print('RESET...')
    elif arg_list[0] == 'SETDEFAULT':
        print('Takes one argument of profile name to be set as the new default profile loaded on launch.\n' +
              'Both profile names and file names(with extensions) are valid.\n' +
              '\tSETDEFAULT <PROFILENAME> - Sets the default profile to be the new profile loaded at launch\n')
    elif arg_list[0] == 'STOP':
        print('STOP...')
    elif arg_list[0] == 'QUIT':
        print('QUIT...')
    else:
        print('Help doesn\'t recognize this command. Try typing \'HELP\' to see a list of valid commands.')

# Load the profile with the passed in name, returns a boolean and if successful a Profile as well
def load(input_list):
    arg_list = parse_args(input_list)
    if len(arg_list) < 1:
        print('No profile name entered.')
        return False, None
    file_name = make_txt_file_name(arg_list[0])
    file_path = './profiles/' + file_name
    if file_exists(file_name, './profiles/'):
        result = map_read_profile(file_path)
        if result[0]:
            loaded_profile = result[1]
            return True, loaded_profile
    print('Error: Profile failed to read.')
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
        result = load(input_list)
        if result[0]:  # On a successful load
            active_profile = result[1]
        else:
            print('Error: Failed to load passed in profile.')
    file_name = active_profile.get_name() + '.txt'
    selected_y = False
    while not selected_y:
        user_input = input(
            'This action cannot be undone, do you want to randomize the priorities of \'' + file_name +
            '(y/n)? ').upper()  # Uppercase for easy recognition
        if user_input == 'Y':
            selected_y = True
        elif user_input == 'N':
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

# Note: This takes a single, optional argument of profile name (or file name) and resets the priorities all to 99.
# FIXME - Should ask the user (y/n) for confirmation
def reset():
    return False

# Note: Takes a single argument of profile_name and sets that profile as the default
# Note: Accepts both profile names and profile file names
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

# Takes no parameters. It starts the bot, creating a path between hotspots based on the active profile's settings
# It should mainly consider priority, proximity, and whether some skills are set as 'active' (to be implemented)
# FIXME - Should this take a profile name as a parameter? It seems like overkill, why even load profiles, then?
def start():
    return False

# FIXME - Want to be able to pause all operations and allow user to manually control their computer
def stop():
    return False
