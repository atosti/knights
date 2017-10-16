import handler
import image

# ToDo ---Issues to be implemented on github---:
# FIXME - Many of the command functions print errors, instead these should be properly captured by exception handling
# FIXME - Build automated tests for each command so they can be quickly tested as we change how functions work
# FIXME - Create functions to resize windows, so that screenshots are all uniform
# FIXME - Allow profiles to be created without usernames passed in
# FIXME - Consider splitting handler into two files, one for commands() and one for all the helpers
# FIXME - Also, all the py files should be moved to a src folder, but then file paths must be adjusted in many places,
# FIXME   this might be easier to implement after automated testing, so we can at a glance know what to fix.
# FIXME - Consider allowing people to pass profile names that are surrounded in quotes to allow for spaces.
# FIXME   Honestly, though. This is a lot of work for almost zero gain. Put it as a LOW priority.
# FIXME - Implement a command to change whether skills are enabled or disabled

# Run initialization
result = handler.initialization('initialization.txt', '../resources/')
if not result['success']:
    print('Error: '+ result['error'])
active_profile = result['profile']

# User input loop
user_input = 'NONE'
input_list = user_input
cmd = user_input
while cmd != "QUIT":
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
    elif cmd == 'LOAD':
        result = handler.load_command(input_list)
        if result[0]:  # Successful load
            active_profile = result[1]
    elif cmd == 'LOGIN':
        handler.login(input_list)
    elif cmd == 'PRINT':
        handler.print_command(input_list, active_profile)
    elif cmd == 'PRIO':
        handler.prio(input_list, active_profile)
    elif cmd == 'RANDOMIZE':
        handler.randomize(input_list, active_profile)
    elif cmd == 'RESETPRIO':  # FIXME - This needs a better name
        results = handler.resetprio(input_list, active_profile)
        if result['success']:
            active_profile = result['profile']
    elif cmd == 'SETDEFAULT':
        handler.setdefault(input_list)
    elif cmd == 'SETNAME':
        handler.setname(input_list, active_profile)
        if result['profile']:
            active_profile = result['profile']
        else:
            print('Error: ' + results['error'])
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
print('Goodbye!')
