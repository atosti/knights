import handler
import profile
import image

# Note: When adding a randomize() command to create random priorities, it's important to also add a way for skills to
#       be toggled as inactive, or ignored. That way a character doesn't waste its time on skills that people deem
#       unimportant to them. This might be best added as a parameter to Skills.
# Note: Profile names must be the same as their file name in order for many commands to work
# Note: Many of the command() functions print errors, these should be properly captured by exception handling
# Note: Thinking about how the bots will function, it will be prudent to set desired levels for each skill, as well
#       as an 'active' status on each skill. That way players can toggle some skills off from being trained. This
#       will allow certain things, such as puring skills, to be much more manageable.
# Note: Eventually, there should maybe be options about whether the bot should use cash from the bank in order to
#       fund its objectives, or whether it should just gather everything itself. This is a ways off, but the process
#       for how we want to do things should be outlined so we don't have to rebuild later.
# Note: Bot action examples
#       1. Skilling
#           a. Bot determines which skill to train, then selects a method for training (e.g. Mine iron, specifically)
#           b. It then checks whether it has all the proper tools to perform that method (e.g. leveled pickaxe)
#               - If not, it checks its bank, then it either buys them or goes to a basic spawn for it
#                   - If no spawn exists, it focuses on getting some cash to afford it
#           c. Then it goes to a 'hotspot' for that skill and begins training
#           d. After it reaches its goal
#               - Later, we would want to add limits on time or exp in order to limit suspicion and to change what
#                 the bot is doing more regularly, even though it wouldn't be the most optimal.
# Note: Another functionality that needs to be addressed is resizing windows from within python, so that we can ensure
#       the screenshots are all the same size and can be hardcoded to a default size.
# FIXME - Update default.txt to use the term HITPOINTS instead of HEALTH in git
# FIXME   it should also really be renamed 'example.txt' it's no longer referenced as a default file.
# FIXME   Although, having a copy of what the default values are to show users IS important.


# FIXME - Only for testing, this will likely go into helper
image.screenshot(__name__)

# Run initialization
result = handler.initialization('initialization.txt', './')
if not result[0]:
    print('Error: An initialization parameter failed to load. Check \'initialization.txt\' is correctly formatted.')
active_profile =result[1]

# User input loop
user_input = 'NONE'
input_list = user_input
while input_list[0] != "QUIT":
    user_input = input('Commands: ')
    input_list = user_input.split(" ")
    # FIXME - Consider changing input_list[0] into a variable, would it prevent needless re-fetching?
    input_list[0] = input_list[0].upper()  # Uppercase the command for easy recognition
    if input_list[0] == 'AUTO':
        handler.auto()
    elif input_list[0] == 'CREATE':
        handler.create(input_list)
    elif input_list[0] == 'DELETE':
        handler.delete(input_list)
    elif input_list[0] == 'HELP':
        handler.help_command(input_list)
    elif input_list[0] == 'LOAD':  # FIXME - Is there a way to move this logic into handler? I need an obj here, though
        result = handler.load(input_list)
        if result[0]:  # Successful load
            active_profile = result[1]
    elif input_list[0] == 'LOGIN':
        handler.login(input_list)
    elif input_list[0] == 'PRINT':
        handler.print_command(input_list, active_profile)
    elif input_list[0] == 'PRIORITY':
        handler.priority(input_list)
    elif input_list[0] == 'RANDOMIZE':
        handler.randomize(input_list, active_profile)
    elif input_list[0] == 'RESET':
        handler.reset(input_list)
    elif input_list[0] == 'SETDEFAULT':
        handler.setdefault(input_list)
    elif input_list[0] == 'STOP':
        handler.stop()
    elif input_list[0] != 'QUIT':  # This is the final check, keep it at the end
        print("Unrecognized command. Type 'help' for more commands or 'quit' to exit.")
