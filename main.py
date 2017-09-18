import handler
import profile

# Note: When adding a randomize() command to create random priorities, it's important to also add a way for skills to
#       be toggled as inactive, or ignored. That way a character doesn't waste its time on skills that people deem
#       unimportant to them. This might be best added as a parameter to Skills.
# Note: Profile names must be the same as their file name in order for some functionalities (such as PRINT) to work

# Run initialization
result = handler.initialization('initialization.txt', './')
if not result[0]:
    print('Error: An initialization parameter failed to load. Check \'initialization.txt\' is correctly formatted.')
active_profile =result[1]

# User input loop
user_input = 'NONE'  # Initialized to dummy value for index to be in range
input_list = user_input
while input_list[0] != "QUIT":
    user_input = input('Commands: ')
    input_list = user_input.split(" ")
    input_list[0] = input_list[0].upper()  # Uppercase the command for easy recognition
    if input_list[0] == 'AUTO':
        handler.auto()
    elif input_list[0] == 'CREATE':
        handler.create(input_list)
    elif input_list[0] == 'DELETE':
        handler.delete(input_list)
    elif input_list[0] == 'SETDEFAULT':
        handler.setdefault(input_list)
    elif input_list[0] == 'HELP':
        handler.help_command(input_list)
    elif input_list[0] == 'LOAD':
        result = handler.load(input_list, active_profile)
    elif input_list[0] == 'LOGIN':
        handler.login(input_list)
    elif input_list[0] == 'PRINT':
        handler.print_command(input_list, active_profile)
    elif input_list[0] == 'PRIORITY':
        handler.priority(input_list)
    elif input_list[0] == 'STOP':
        handler.stop()
    elif input_list[0] != 'QUIT':  # This is the final check, keep it at the end
        print("Unrecognized command. Type 'help' for more commands or 'quit' to exit.")
