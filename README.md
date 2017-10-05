# knights
This is a program designed to automate many of RS's actions and aims to allow fully functional bots to maintain their own paths based on a few initial goals set for them to follow.

## Working Functionality
Although many of these things will likely be reworked and revised in the future, they're currently working smoothly.
### Commands:
 * CREATE - Creates a new profile.
 * DELETE - Deletes a profile.
 * HELP - Gives information on how the commands are used.
 * LOAD - Loads a profile as the active profile.
 * PRINT - Prints the contents of a profile to the console.
 * RANDOMIZE - Randomizes the priorities of a profile.
 * RESETPRIO - Resets all the priorities to 99 for a profile.
 * SETDEFAULT - Sets the default profile loaded on launch.
 * SETNAME - Changes the name of a profile.
 * SETUSERNAME - Changes the username of a profile.
 * QUIT - Exits the program.

## Documentation
This documentation is currently a list of design practices and unique functionality (oddities) of the program. With time it will be more refined including things like a quickstart guide.

### Design Practices and Oddities
1. All commands look only at the first arguments passed to them, any excess is ignored.
    * Additionally the order of flags and arguments matters.
2. All commands **are not** case sensitive. This is for ease-of-use by the user and uniformity in the code.
    * However, user information (e.g. profile names, usernames, etc.) **are** case-sensitive and should be kept this way.
3. If a function returns a Tuple, its first index should always correspond to its success boolean.
4. Valid skill priorities are integers in the range 0 to 99. 
   * Highest priority corresponds to 0 and 99 corresponds to lowest priority.
5. Profiles are txt files that store information about a character and its objectives.
   * It's fine for a username to be associated with multiple profiles. This will create more dynamic paths to objectives as a user's goals and preferences (in the profile) change.
   * Currently, only .txt files are accepted as profile file types.
6. DEFAULT_PROFILE in initialization.txt takes file names and not profile names. As such, they must have a file extension
7. For commands that deal with profiles, if no argument is passed to them, they should use the active profile by default.
8. Commands that make large changes to files should always prompt the user (y/n) before executing.
    * This is especially relevant for operations that are impossible to undo.
9. Profile names must be the same as their file name in order for many commands to function properly
10. The function priority() can take a mix of integers and skill-names.
    * Ex: 'attack defence 10 20 cooking 30' is interpreted as 'attack=10, defence=20, cooking=30'
    * This function also ignores misspelled skill names and their corresponding integer

## Features to be Implemented
See issues labeled [enhancement](https://github.com/atosti/knights/issues?q=is%3Aopen+is%3Aissue+label%3Aenhancement).

## Bugs
Most of these are well-documented via FIXMEs in the source, which will always be more up-to-date than this file. As such, unless a bug becomes large or affects a significant portion of functionality, it will not be listed here.
