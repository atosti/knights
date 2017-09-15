import skill
class Profile:

    # FIXME - Take another parameter, like username, that allows a character to be searched and have their data fetched
    # FIXME - Actually, have a helper func that searches everything and passes it all to the Profile
    def __init__(self, name, username, password, skill_list, combat_level):
        self.name = name  # The name of this profile
        self.username = username  # The username of the RS character
        self.password = password
        self.skill_list = []
        self.add_skills(skill_list)
        self.combat_level = combat_level

    def add_skills(self, skill_list):
        self.skill_list.append(skill_list[0])
        self.skill_list.append(skill_list[1])
        self.skill_list.append(skill_list[2])
        self.skill_list.append(skill_list[3])
        self.skill_list.append(skill_list[4])
        self.skill_list.append(skill_list[5])
        self.skill_list.append(skill_list[6])
        self.skill_list.append(skill_list[7])
        self.skill_list.append(skill_list[8])
        self.skill_list.append(skill_list[9])
        self.skill_list.append(skill_list[10])
        self.skill_list.append(skill_list[11])
        self.skill_list.append(skill_list[12])

    # FIXME - There should be an update for all the fields of Profile
    # FIXME - This update should check there are no other profiles with this name, or a helper could do this
    # FIXME - If a helper does this, then ensure this is only ever called with valid parameters
    def set_username(self, username):
        self.username = username

    def get_combat_level(self):
        return self.combat_level

    def get_name(self):
        return self.name

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_skill_list(self):
        return self.skill_list
