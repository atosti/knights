import image
import mouse
import profile
import skill
import os  # Used to check if a file is empty
import random  # Used for random number generation


# ---Helper Functions---
# FIXME - implement this into initialization AND load
# Checks if a file exists, must be passed the full file name for this to work
def file_exists(file_name, dir_path):
    for file in os.listdir(dir_path):
        if file.startswith(file_name):
            return True
    return False


def file_is_empty(file_path):
    return os.stat(file_path).st_size == 0


# FIXME - How to return a Tuple full of objects that may or may not exist depending on various function calls,
# FIXME     is the only way to do a large if/else statement? This will matter if I expand this function.
# Read the initialization file and set a default profile as current_profile
def initialization(file_name, dir_path):
    if not file_exists(file_name, dir_path):  # Check the file exists before attempting to read it
        return False, None
    file_path = dir_path + file_name
    with open(file_path) as f:
        init_content = f.read().splitlines()
        for i in range(0, len(init_content)):
            inner = init_content[i].split('=')
            if inner[0] == 'DEFAULT_PROFILE':
                default_profile_path = './profiles/' + inner[1]
                result = read_profile(default_profile_path)  # Load the default profile
                if result[0]:
                    current_profile = result[1]
                else:
                    # FIXME - How to get it so users can reset initialization and default.txt files automatically
                    # print('Error: Failed to load default profile, reset initialization.txt and default.txt')
                    1  # Placeholder
    if result[0]:  # This belongs at the end, because it's the Tuple returned for ALL of initialization's actions
        return True, current_profile
    return False, None


# FIXME - Check that the file doesn't already exist, and if it does maybe just overwrite or return an error
# FIXME     implement password and change the format of the file being generated to match the new format
# FIXME - This needs a better name, but I don't know what to call it
# Creates a new profile file
def new_profile_file(profile):
    with open('profiles/' + profile.name + '.txt', 'w+') as f:
        f.write('NAME=' +                   profile.name +
                '\nUSERNAME=' +             profile.get_username() +
                '\nPASSWORD=' +             profile.get_password() +
                '\nCOMBAT_LEVEL=' +         str(profile.get_combat_level()) +
                '\nATTACK=' +               str(profile.skill_list[0].level) +
                '\nATTACK_PRIO=' +          str(profile.skill_list[0].priority) +
                '\nCRAFTING=' +             str(profile.skill_list[1].level) +
                '\nCRAFTING_PRIO=' +        str(profile.skill_list[1].priority) +
                '\nDEFENCE=' +              str(profile.skill_list[2].level) +
                '\nDEFENCE_PRIO=' +         str(profile.skill_list[2].priority) +
                '\nFISHING=' +              str(profile.skill_list[3].level) +
                '\nFISHING_PRIO=' +         str(profile.skill_list[3].priority) +
                '\nHEALTH=' +               str(profile.skill_list[4].level) +
                '\nHEALTH_PRIO=' +          str(profile.skill_list[4].priority) +
                '\nMAGIC=' +                str(profile.skill_list[5].level) +
                '\nMAGIC_PRIO=' +           str(profile.skill_list[5].priority) +
                '\nMINING=' +               str(profile.skill_list[6].level) +
                '\nMINING_PRIO=' +          str(profile.skill_list[6].priority) +
                '\nPRAYER=' +               str(profile.skill_list[7].level) +
                '\nPRAYER_PRIO=' +          str(profile.skill_list[7].priority) +
                '\nRANGE=' +                str(profile.skill_list[8].level) +
                '\nRANGE_PRIO=' +           str(profile.skill_list[8].priority) +
                '\nRUNECRAFTING=' +         str(profile.skill_list[9].level) +
                '\nRUNECRAFTING_PRIO=' +    str(profile.skill_list[9].priority) +
                '\nSMITHING=' +             str(profile.skill_list[10].level) +
                '\nSMITHING_PRIO=' +        str(profile.skill_list[10].priority) +
                '\nSTRENGTH=' +             str(profile.skill_list[11].level) +
                '\nSTRENGTH_PRIO=' +        str(profile.skill_list[11].priority) +
                '\nWOODCUTTING=' +          str(profile.skill_list[12].level) +
                '\nWOODCUTTING_PRIO=' +     str(profile.skill_list[12].priority)
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


# FIXME - Skill_list is appended via alternation, find a more elegant way to do this that isn't hardcoded to a pattern
# Reads the content from a profile file and returns a Skill object
def read_profile(file_path):
    skill_list = []
    username = ''
    profile_name = ''
    password = ''
    skill_name = ''
    level = 0  # Initialized to invalid values
    current_priority = -1  # Initialized to invalid values
    with open(file_path) as f:
        line = f.read().splitlines()
        for i in range(0, len(line)):
            inner_line = line[i].split('=')
            if inner_line[0] == 'NAME':
                profile_name = inner_line[1]
            elif inner_line[0] == 'USERNAME':
                username = inner_line[1]
            elif inner_line[0] == 'PASSWORD':
                password = inner_line[1]
            elif inner_line[0] == 'COMBAT_LEVEL':
                combat_level = inner_line[1]
            elif inner_line[0] == 'ATTACK':
                skill_name = inner_line[0]
                level = inner_line[1]
            elif inner_line[0] == 'ATTACK_PRIO':
                current_priority = inner_line[1]
            elif inner_line[0] == 'CRAFTING':
                skill_name = inner_line[0]
                level = inner_line[1]
            elif inner_line[0] == 'CRAFTING_PRIO':
                current_priority = inner_line[1]
            elif inner_line[0] == 'DEFENCE':
                skill_name = inner_line[0]
                level = inner_line[1]
            elif inner_line[0] == 'DEFENCE_PRIO':
                current_priority = inner_line[1]
            elif inner_line[0] == 'FISHING':
                skill_name = inner_line[0]
                level = inner_line[1]
            elif inner_line[0] == 'FISHING_PRIO':
                current_priority = inner_line[1]
            elif inner_line[0] == 'HEALTH':
                skill_name = inner_line[0]
                level = inner_line[1]
            elif inner_line[0] == 'HEALTH_PRIO':
                current_priority = inner_line[1]
            elif inner_line[0] == 'MAGIC':
                skill_name = inner_line[0]
                level = inner_line[1]
            elif inner_line[0] == 'MAGIC_PRIO':
                current_priority = inner_line[1]
            elif inner_line[0] == 'MINING':
                skill_name = inner_line[0]
                level = inner_line[1]
            elif inner_line[0] == 'MINING_PRIO':
                current_priority = inner_line[1]
            elif inner_line[0] == 'PRAYER':
                skill_name = inner_line[0]
                level = inner_line[1]
            elif inner_line[0] == 'PRAYER_PRIO':
                current_priority = inner_line[1]
            elif inner_line[0] == 'RANGE':
                skill_name = inner_line[0]
                level = inner_line[1]
            elif inner_line[0] == 'RANGE_PRIO':
                current_priority = inner_line[1]
            elif inner_line[0] == 'RUNECRAFTING':
                skill_name = inner_line[0]
                level = inner_line[1]
            elif inner_line[0] == 'RUNECRAFTING_PRIO':
                current_priority = inner_line[1]
            elif inner_line[0] == 'SMITHING':
                skill_name = inner_line[0]
                level = inner_line[1]
            elif inner_line[0] == 'SMITHING_PRIO':
                current_priority = inner_line[1]
            elif inner_line[0] == 'STRENGTH':
                skill_name = inner_line[0]
                level = inner_line[1]
            elif inner_line[0] == 'STRENGTH_PRIO':
                current_priority = inner_line[1]
            elif inner_line[0] == 'WOODCUTTING':
                skill_name = inner_line[0]
                level = inner_line[1]
            elif inner_line[0] == 'WOODCUTTING_PRIO':
                current_priority = inner_line[1]
            else:
                return False, None
            if (i % 2) == 1:  # Every two lines, append a skill onto the skill_list
                skill_list.append(skill.Skill(skill_name, current_priority, level))
    loaded_profile = profile.Profile(profile_name, username, password, skill_list, combat_level)
    return True, loaded_profile


# FIXME - Need to read the values, pass them into a list of skills, then put them into a profile to be returned
# FIXME - This is largely deprecated, it's probably better to just start new
def update_profile(file_path):
    with open(file_path) as f:
        content = f.read().splitlines()
    skill_priority_file = open(file_path, "w+")  # If file doesn't exist, it will be created
    contents = skill_priority_file.readlines()
    skill_priority_file.close()  # Mandatory file close
    print("File contains: " + contents)
    skill_name = []
    skill_priority = []
    skill_list = []
    for i in range(0, 13):  # i*2 holds the index of the skill name, adding 1 gives the corresponding priority
        # FIXME - Add a way to fetch level (it should probably reference an image class, or the highscores api?)
        current_skill = skill.Skill(contents[i * 2], contents[(i * 2) + 1], 1)  # name, priority, level
        skill_list.append(current_skill)
    return profile.Profile(skill_list, 3)  # FIXME - Find a way to fetch combat level


# ---Functions for Commands---
def auto():  # Allows the system to take control, deciding the best course of action for the character
    return False
    # Create and populate a list of objectives based on user-set goals via the commandline
    # Then either select one at random (to avoid detection) or create an optimal path between the tasks


# FIXME - This followed an old format, I'm not sure if it's still valid
# FIXME     if a profile has no password passed for it, then it should just auto assign a dummy value
# FIXME - Implement fetching skill levels from searching the username in an API or from screen capture
# FIXME     they're currently just hardcoded to default values. Could also set prios to random values (I built a func for that)
def create(input_list):
    arg_list = parse_args(input_list)
    if len(arg_list) < 2:
        print("Too few arguments, pass the profile_name and username after the command")
        return False
    # FIXME - Check if the profile name already exists in a new elif
    else:
        profile_name = 'BLANK'
        username = 'BLANK'
        password = 'BLANK'
        for i in range(0, len(arg_list)):
            if i == 0:
                profile_name = arg_list[i]
            elif i == 1:
                username = arg_list[i]
            elif i == 2:
                password = arg_list[i]
        skill_list = []
        skill_list.append(skill.Skill("ATTACK", 99, 1))
        skill_list.append(skill.Skill("CRAFTING", 99, 1))
        skill_list.append(skill.Skill("DEFENCE", 99, 1))
        skill_list.append(skill.Skill("FISHING", 99, 1))
        skill_list.append(skill.Skill("HEALTH", 99, 1))
        skill_list.append(skill.Skill("MAGIC", 99, 1))
        skill_list.append(skill.Skill("MINING", 99, 1))
        skill_list.append(skill.Skill("PRAYER", 99, 1))
        skill_list.append(skill.Skill("RANGE", 99, 1))
        skill_list.append(skill.Skill("RUNECRAFTING", 99, 1))
        skill_list.append(skill.Skill("SMITHING", 99, 1))
        skill_list.append(skill.Skill("STRENGTH", 99, 1))
        skill_list.append(skill.Skill("WOODCUTTING", 99, 1))
        new_profile = profile.Profile(profile_name, username, password, skill_list, 3)
        new_profile_file(new_profile)
        return True


# FIXME - Takes a single argument of profile_name and assigns that as the default profile to be loaded in
def default(input_list):
    return False


# FIXME - This should check if the deleted profile is the default one, and then reset the default profile if so
# FIXME - This should check if they entered a file name (ends in .txt) and if so it should let them use it (as long as its valid)
def delete(input_list):
    arg_list = parse_args(input_list)
    file_name = arg_list[0] + '.txt'
    if file_exists(file_name, './profiles/'):
        y_or_n = False
        while not y_or_n:
            user_input = input(
                'This action cannot be undone, do you want to delete \'' + file_name + '\'(y/n)? ').upper()
            if user_input == 'Y':
                file_path = './profiles/' + file_name
                os.remove(file_path)  # Perform the delete
                return True
            elif user_input == 'N':
                return False
            if user_input == 'Y' or user_input == 'N':
                y_or_n = True
    else:
        print('Error: Profile \'' + file_name + '\' not found.')
        return False


# FIXME - Many commands remain without explanations, fill them in or delelte them as development progresses
def help_command(input_list):
    arg_list = parse_args(input_list)
    if len(arg_list) < 1:  # If no arguments, then print general help
        print('AUTO\t\tAllows the system to automatically create objectives and work to complete them\n'
              'CREATE\t\tTakes two arguments (profile_name, username) to create a profile with that character\'s data\n'
              'DEFAULT\t\tTakes one argument (profile_name) to set a profile as the default one loaded on launch\n'
              'DELETE\t\tTakes one argument (profile_name) and deletes the profile from the system'
              'HELP\t\tProvides a list of commands and how to use them\n'
              'LOAD\t\tTakes one argument (profile_name) and loads that profile\n'
              'LOGIN\t\tTakes two arguments (username, password) and logs in the user\n'  # FIXME - Take an optional parameter for world number
              'PRINT\t\tTakes one argument (profile_name) and prints its contents.\n'
              'PRIORITY\tTakes a list of skills and priorities\n'
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
    elif arg_list[0] == 'DEFAULT':
        print('DEFAULT...')
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
        print('PRINT...')
    elif arg_list[0] == 'PRIORITY':
        print('PRIORITY...')
    elif arg_list[0] == 'STOP':
        print('STOP...')
    elif arg_list[0] == 'QUIT':
        print('QUIT...')
    else:
        print('Help doesn\'t recognize this command. Try typing \'HELP\' to see a list of valid commands.')


# Load the profile with the passed in name, returns a boolean and if successful a Profile as well
def load(input_list):
    arg_list = parse_args(input_list)
    if len(arg_list) <= 0:
        print("No profile name entered. Type \"LOAD <profile_name>\" to run this command.")
        return False, None
    else:
        # FIXME - Add a condition that if it includes the '.txt' already, then to just take the whole arg as the path
        file_name = arg_list[0] + '.txt'
        file_path = './profiles/' + file_name
        if file_exists(file_name, './profiles/'):
            result = read_profile(file_path)
            if result[0]:
                loaded_profile = result[1]
                return True, loaded_profile
    print("Error: Profile failed to read. Try using DELETE and CREATE commands to regenerate the profile.")
    return False, None


def login(input_list):
    # Want to log in the user with command line arguments, then wait for more input from the user
    # login(user, pass) and maybe an optional third parameter for world number
    return False


# FIXME - Initialize priorities to values that follow a hardcoded "optimal" route based on testing/timing routes
# FIXME - Looking back at this, I'm not sure what it should do, this might just be consolidated into AUTO later
def optimize():
    return False


# FIXME - If no argument is passed to PRINT, it will use the current profile if one is loaded
def print_command(input_list):
    # If no argument is passed to PRINT, it will use the active profile if one is loaded, else it will fail
    return False


# This sets the priority of various skills to
def priority(input_list):
    # FIXME - Have this take a list of <skill prio, skill prio, skill prio> and optionally a character name
    # This will open the file for the proper profile, then find the skilsl that match its args and assign the new priority
    return False
    # This should take a series of flags as inputs, such as character name
    file_open("skill_priorities.txt")  # FIXME - On hold until profiles are done


# FIXME - Want to be able to pause all operations and allow user to manually control their computer
def stop():
    return False

