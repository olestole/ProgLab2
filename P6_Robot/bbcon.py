"""The highest-level class, BBCON (Behavior-Based Controller)"""

import time

from arbitrator import Arbitrator
from sensob import Sensob

from Help_Classes.motors import Motors
from Help_Classes.ultrasonic import Ultrasonic


class BBCON:

    behaviors = []
    active_behaviors = []
    sensobs = []
    motobs = None
    arbitrator = None


    def __init__(self):
        """ init """
        self.arbitrator = Arbitrator(self)
        ultra = Ultrasonic()
        sensob = Sensob(ultra)
        sensob.update()
        value = sensob.get_value()
        print("Value: ", value)

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
        self.arbitrator.choose_action(self.active_behaviors)
        #TODO: Update the motobs based on these motor recommendations
        time.sleep(0.5)
        #TODO: Reset the sensobs


def main():
    bbcon = BBCON()
    print("MAIN")
    dancer()


if __name__ == "__main__":
    main()
