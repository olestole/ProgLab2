"""The highest-level class, BBCON (Behavior-Based Controller)"""


class BBCON:

    def __init__(self, arbitrator):
        self.behaviors = []
        self.active_behaviors = []
        self.sensobs = []
        self.motobs = []
        self.arbitrator = arbitrator

    def add_behavior(self):
        """append a newly-created behavior onto the behaviors list"""

    def add_sensob(self):
        """append a newly-created sensob onto the sensobs list"""

    def activate_behavior(self):
        """add an existing behavior onto the active-behaviors list"""

    def deactive_behavior(self):
        """remove an existing behavior from the active behaviors list"""

    def run_one_timestep(self):
        """constitutes the core BBCON activity"""
