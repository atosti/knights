# knights
This is a program designed to automate many of RS's actions and aims to allow fully functional bots to maintain their own paths based on a few initial goals set for them to follow.

## Completed Functionality
Currently the CREATE and LOAD commands are implemented allowing users to create profiles and load them for accessing via other commands.

Additionally, DELETE was just implemented and should be working correctly now, allowing users to delete a profile by specifying its name

## Docs
Currently the docs are simply a series of good practices and oddities related to this project. As such, they will be listed numerically for now.
1. All commands will only look at the first arguments passed to them, any excess will be ignored.
    * Additionally the order of flags/arguments matters as well, so it's important to be precise
2. All commands are case-insensitive for ease-of-use and uniformity in the code
    * However, names, usernames, passwords, etc. passed by the user **ARE** case-sensitive
3. All commands should return a boolean as their first index [0] if they're returning a Tuple
    * Also, for all functions that return Tuples, when they trigger False they should return 'None' in place of the desired object (e.g. 'return False, None')
4. Priorities have an integer value in the range 0 to 99, with 0 being highest and 99 being lowest priority
5. Profiles are a customized list of priorities, skill levels, and other character information
    * It is valid to have multiple profiles for a single character. This allows users to load different priorities of their choosing
6. When adding or removing a COMMAND be sure to also add or remove it from the HELP command
    * Add both a short general explanation and a more detailed one for if HELP <COMMAND_NAME> is called

## Features to be Implemented and Bugs to Fix
1. The HELP command should be clear about the order of arguments mattering and that excess arguments are ignored
2. Add a flag option for priorities to be randomized on creation of a profile
    * Alternately, this could even be its own command to be run on the currently loaded profile
3. Profile initialization currently intializes everything to level 1 at lowest priority rather than fetching the values
4. Currently only F2P skills are considered, but implement functionality for member's skills to be considered
5. Helper functions need to be implemented to read images from the screen and determine the player's location
6. Functions need to be written to move pre-set distances (e.g. moving X many tiles to the North)
7. Have a flag to determine if a user is f2p or not
8. Automatically ask the user (y/n) if they want to create a new profile when the profile they tried to load doesn't exist
9. Currently the entire command (user_input) is passed to the handler, maybe just the arg list should be passed
10. Implement HELP <COMMAND_NAME> to offer more info on each command
11. Create a command for allowing the user to change the default file that gets loaded each time the program is run
12. Add a way for users to change a profile's name, but check that the profile name doesn't exist already AND change the file name to match
13. Find a way to make the original default profile read-only so that it cannot be easily modified by users
14. None of my index calls for profile creation and loading are checking if the indices exist, so if a user changes the profile txt files manually, then the program can crash
15. Look back at the classes you've made, make them private, and then use the proper getters/setters to access data

There are a variety of other issues, but they're all marked with FIXMEs in the code near where the problem exists.
