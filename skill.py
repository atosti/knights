class Skill:
    def __init__(self, name, priority, level):
        self.name = name.upper()
        self.priority = priority
        self.level = level
        self.f2p = True  # FIXME - Implement the ability for skills to be non-f2p

    def set_name(self, name):
        self.name = name

    def set_priority(self, priority):
        self.priority = priority

    def set_level(self, level):
        self.level = level

    def get_name(self):
        return self.name

    def get_priority(self):
        return self.priority

    def get_level(self):
        return self.level

    # FIXME - Create a better name for swapping from f2p to membs
    def switch_f2p_status(self):
        self.f2p = not self.f2p
