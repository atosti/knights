# General Thoughts:
# Note: This is currently an outline of some functionality I image auto() using. It will likely change in the future.
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

# FIXME - A priority should maybe be taken to ensure safety, so if logging into combat, the bot should stop whatever
# FIXME   it's doing and focus on survival.
# Initial steps taken to setup the bot
def initialize():
    # Log the player in with their credentials (or prompt the user for them, then login)
    # Center the screen and zoom all the way out
    # Find its location in the world
    # Check its priorities against its goals and update its immediate objective (this could be a list of a few)
    # Based on its priorities, head to one of a handful of hotspots (to improve variance) that match its current level
    # Train until its goal is met OR add functionality to rotate to its next most immediate skill goal after a few hrs
    # Log out after a certain amount of hours have been reached to avoid suspicion.
    #   - The user should have control over this number of hours if they want to change it.
    #   - Also have a max consecutive hrs value and a max total hrs per day value

    return {'success': False}
