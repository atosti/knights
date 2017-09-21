class Skill:
    def __init__(self, name, priority, level):
        self.active = True  # FIXME - Implement the ability for skills to be enabled/disabled
        self.goal = 1  # FIXME - Implement the ability for target level to be changed
        self.level = level
        self.f2p = True  # FIXME - Implement the ability for skills to be non-f2p
        self.name = name.upper()
        self.priority = priority

    def get_active(self):
        return self.active

    def get_goal(self):
        return self.active

    def get_level(self):
        return self.level

    def get_name(self):
        return self.name

    def get_priority(self):
        return self.priority

    def set_active(self, active):
        self.active = active

    def set_goal(self, goal):
        self.goal = goal

    def set_level(self, level):
        self.level = level

    def set_name(self, name):
        self.name = name

    def set_priority(self, priority):
        self.priority = priority

    # FIXME - Create a better name for swapping from f2p to membs
    def switch_f2p_status(self):
        self.f2p = not self.f2p
