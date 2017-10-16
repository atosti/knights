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

    def __eq__(self, other): 
            return (self.name == other.name and
            self.username == other.username and
            self.password == other.password and
            self.skill_dict == other.skill_dict and
            self.combat_level == other.combat_level)

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

    def request_skills(self):
        r = requests.get('http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player=' + self.username)
        skill_list = []
        if r.status_code == 200:
             full_text = r.text
             raw_skill_list = full_text.split('\n')
             return {
                 'success': True,
                 'raw_skill_list': raw_skill_list,
                 'error': ''}
        else:
            return {
                'success': False,
                'raw_skill_list': [],
                'error': 'Request to server failed, error code: '+ r.status_code}

    def process_skills(self, raw_skill_list):
        index = 0
        raw_dict = {}
        for item in raw_skill_list:
            raw_dict[index] = item
            index+=1
        skill_list = [
            'Overall','Attack','Defence',
            'Strength','Hitpoints','Ranged',
            'Prayer','Magic','Cooking',
            'Woodcutting','Fletching','Fishing',
            'Firemaking','Crafting','Smithing',
            'Mining','Herblore','Agility',
            'Thieving','Slayer','Farming',
            'Runecraft','Hunter','Construction']
        processed_dict = {}
        for index in range(0,len(skill_list)):
            key = skill_list[index]
            value = self.__process_raw_skill(raw_dict[index])
            processed_dict[key] = value
        return processed_dict

    def __process_raw_skill(self, raw_element):
        split = raw_element.split(',')
        if len(split) == 3:
            element_dict = {}
            element_dict['Rank'] = split[0]
            element_dict['Level'] = split[1]
            element_dict['XP'] = split[2]
            return element_dict
        else:
            return {}
    
    def get_highscore_skills(self):
        request_result = request_skills()
        if(request_result['success'] == True):
            return process_skills(request_result['raw_skill_list'])
        else:
            return request_result

    # FIXME - When calling this update, you should check there are no other profiles with this name
    def set_name(self, name):
        self.name = name

    def set_password(self, password):
        self.password = password

    def set_username(self, username):
        self.username = username
