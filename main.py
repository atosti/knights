import handler
import image

# ToDo ---Issues to implement---:
# FIXME - Many of the command functions print errors, instead these should be properly captured by exception handling
# FIXME - Build automated tests for each command so they can be quickly tested as we change how functions work
# FIXME - Thinking about how the bots will function, implemented desired levels for each skill to be leveled to.
# FIXME - Create functions to resize windows, so that screenshots are all uniform
# FIXME - Allow profiles to be created without usernames passed in
# Note: Consider allowing people to pass profile names that are surrounded in quotes to allow for spaces.
#       Honestly, though. This is a lot of work for almost zero gain.
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


# Successfully takes a screenshot, commented out for now but it works fine
# image.screenshot(__name__)

# Run initialization
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
    cmd = input_list[0].upper()  # Uppercase the command for easy recognition
    if cmd == 'AUTO':
        handler.auto()
    elif cmd == 'CREATE':
        handler.create(input_list)
    elif cmd == 'DELETE':
        handler.delete(input_list)
    elif cmd == 'HELP':
        handler.help_command(input_list)
    elif cmd == 'LOAD':  # FIXME - Is there a way to move this logic into handler? I need an obj here, though
        result = handler.load_command(input_list)
        if result[0]:  # Successful load
            active_profile = result[1]
    elif cmd == 'LOGIN':
        handler.login(input_list)
    elif cmd == 'PRINT':
        handler.print_command(input_list, active_profile)
    elif cmd == 'PRIORITY':
        handler.priority(input_list)
    elif cmd == 'RANDOMIZE':
        handler.randomize(input_list, active_profile)
    elif cmd == 'RESETPRIO':  # FIXME - This needs a better name
        results = handler.resetprio(input_list, active_profile)
        if result[0]:
            active_profile = result[1]
    elif cmd == 'SETDEFAULT':
        handler.setdefault(input_list)
    elif cmd == 'SETNAME':
        handler.setname(input_list, active_profile)
        if result[0]:
            active_profile = result[1]
    elif cmd == 'SETUSERNAME':
        results = handler.setusername(input_list, active_profile)
        if results['success']:
            active_profile = results['profile']
        else:
            print('Error: ' + results['error'])
    elif cmd == 'STOP':
        handler.stop()
    elif cmd != 'QUIT':  # This is the final check, keep it at the end
        print("Unrecognized command. Type 'help' for more commands or 'quit' to exit.")
