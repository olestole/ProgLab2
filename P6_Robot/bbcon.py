"""The highest-level class, BBCON (Behavior-Based Controller)"""

import time
from arbitrator import Arbitrator
from R6_Robot.Help_Classes.motors import Motors
from P6_Robot.Help_Classes.robodemo import dancer


class BBCON:

    behaviors = []
    active_behaviors = []
    sensobs = []
    motobs = None
    arbitrator = None


    def __init__(self, arbitrator):
        self.arbitrator = Arbitrator(self)
        self.motobs = Motors()
        self.motobs.forward()

    def add_behavior(self, behavior):
        """append a newly-created behavior onto the behaviors list"""
        self.behaviors.append(behavior)

    def add_sensob(self, sensor):
        """append a newly-created sensob onto the sensobs list"""
        self.sensobs.append(sensor)

    def activate_behavior(self, behavior):
        """add an existing behavior onto the active-behaviors list"""
        self.activate_behavior.append(behavior)

    def deactive_behavior(self, behavior):
        """remove an existing behavior from the active behaviors list"""
        self.activate_behavior.remove(behavior)

    def run_one_timestep(self):
        """constitutes the core BBCON activity"""
        #TODO: Update all sensobs
        #TODO: Update all behaviors
        arbitrator.choose_action(self.active_behaviors)
        #TODO: Update the motobs based on these motor recommendations
        time.sleep(0.5)
        #TODO: Reset the sensobs
