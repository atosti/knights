import skill
import requests
class Profile:

    # FIXME - Actually, have a helper func that searches all player info everything and passes it all to the Profile
    # http://runescape.wikia.com/wiki/Application_programming_interface
    def __init__(self, name, username, password, skill_dict, combat_level):
        self.name = name  # The name of this profile
        self.username = username  # The username of the RS character
        self.password = password
        self.skill_dict = skill_dict
        self.combat_level = combat_level

    def get_combat_level(self):
        return self.combat_level

    def get_name(self):
        return self.name

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_skill_dict(self):
        return self.skill_dict
        
    def get_skill(self, skill_name):
        return self.skill_dict[skill_name]

    # FIXME - Figure out what line correlates to each skill, then have it populate properly. Also have it handle
    # FIXME     whatever the result is when an invalid username is passed.
    def fetch_skills(self):
        r = requests.get('http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player=' + self.username)
        data = r.text
        for i in range(0, len(data)):
            inner = data.split('\n')
            print(str(i) + ': ' + inner[i])
            # Format of the info:
            # 1: (something, total level, total exp)
            # 2: (something, skill_lvl, skill_exp)
            # Some of these have -1 as all the fields, I presume that's if they're unleveled

    # FIXME - This update should check there are no other profiles with this name, or a helper could do this
    # FIXME - If a helper does this, then ensure this is only ever called with valid parameters
    def set_name(self, name):
        self.name = name

    def set_password(self, password):
        self.password = password

    def set_username(self, username):
        self.username = username