import handler
import profile
# FIXME - Double check that no skills were missed for F2P when creating profiles (i.e. check with the game)

# Load default profile
result = handler.initialization('initialization.txt', './')
if result[0]:
    active_profile = result[1]
else:
    print('Error: Default profile failed to load. Please manually load one with LOAD before continuing.')

# User input loop
user_input = 'BLANK'  # Initialized to a dummy value
input_list = user_input
while input_list[0] != "QUIT":
    user_input = input('Commands: ')
    input_list = user_input.split(" ")  # Parse by spaces
    input_list[0] = input_list[0].upper() # Uppercase the command for easy recognition
    if input_list[0] == 'AUTO':
        handler.auto()
    elif input_list[0] == 'CREATE':
        handler.create(input_list)
    elif input_list[0] == 'DELETE':
        handler.delete(input_list)
    elif input_list[0] == 'DEFAULT':
        handler.default(input_list)
    elif input_list[0] == 'HELP':
        handler.help_command(input_list)
    elif input_list[0] == 'LOAD':
        result = handler.load(input_list)
        if result[0]:
            active_profile = result[1]
    elif input_list[0] == 'LOGIN':
        handler.login(input_list)
    elif input_list[0] == 'PRINT':
        handler.print_command(input_list)
    elif input_list[0] == 'PRIORITY':
        handler.priority(input_list)
    elif input_list[0] == 'STOP':
        handler.stop()
    elif input_list[0] != 'QUIT':  # This is the final check, keep it at the end
        print("Unrecognized command. Type 'help' for more commands or 'quit' to exit.")
