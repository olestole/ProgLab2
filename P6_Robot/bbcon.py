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

        #TODO: add more sensobs
        self.add_sensob(Sensob(Ultrasonic()))

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
        for sensob in self.sensobs:
            sensob.update()
            print("Ultrasensor value: ", sensob.get_value())
        
        #TODO: Update all behaviors
        #self.arbitrator.choose_action(self.active_behaviors)
        #TODO: Update the motobs based on these motor recommendations
        time.sleep(0.5)
        #TODO: Reset the sensobs


def main():
    bbcon = BBCON()
    print("MAIN")
    while True:
        bbcon.run_one_timestep()

if __name__ == "__main__":
    main()
