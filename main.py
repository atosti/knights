import handler
import image

# Note: Profile names must be the same as their file name in order for many commands to function properly
# Note: Many of the command functions print errors, these should be properly captured by exception handling
# Note: Thinking about how the bots will function, it will be prudent to set desired levels for each skill.
# Note: Eventually, there should be options about whether the bot should use cash from the bank in order to
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
# Note: Consider allowing people to pass profile names that are surrounded in quotes to allow for spaces.
#       Honestly, though. This is a lot of work for almost zero gain.
# Note: Should we allow profiles to be created without usernames passed in?

# FIXME - Only for testing, this will likely go into helper.py later
# Successfully takes a screenshot, commented out for now but it works fine
# image.screenshot(__name__)

# Run initialization
# FIXME - On init, the default profile should have its skills re-fetched to ensure that the values are up-to-date
result = handler.initialization('initialization.txt', './')
if not result['success']:
    print('Error: '+ result['error'])
    #print('Error: An initialization parameter failed to load. Check \'initialization.txt\' is correctly formatted.')
active_profile = result['profile']

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
        result = handler.load_command(input_list)
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
    elif input_list[0] == 'RESETPRIO':  # FIXME - This needs a better name, esp. if we add multiple reset commands for various fields
        results = handler.resetpriority(input_list, active_profile)
        if result[0]:
            active_profile = result[1]
    elif input_list[0] == 'SETDEFAULT':
        handler.setdefault(input_list)
    elif input_list[0] == 'SETUSERNAME':
        results = handler.setusername(input_list, active_profile)
        if results['success']:
            active_profile = results['profile']
        else :
            print('Error: '+ results['error'])
    elif input_list[0] == 'STOP':
        handler.stop()
    elif input_list[0] != 'QUIT':  # This is the final check, keep it at the end
        print("Unrecognized command. Type 'help' for more commands or 'quit' to exit.")
