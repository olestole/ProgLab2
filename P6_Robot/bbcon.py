"""The highest-level class, BBCON (Behavior-Based Controller)"""

import time

from arbitrator import Arbitrator
from sensob import Sensob
from behavior import Behavior
from motob import Motob

from Help_Classes.motors import Motors

from Help_Classes.camera import Camera
from Help_Classes.reflectance_sensors import ReflectanceSensors 
from Help_Classes.ultrasonic import Ultrasonic
from Help_Classes.zumo_button import ZumoButton

class BBCON:

    def __init__(self):
        """ init """
        self.sensobs = []
        self.add_sensob(Sensob(Ultrasonic()))
        self.add_sensob(Sensob(ReflectanceSensors()))
        #self.add_sensob(Sensob(Camera()))

        self.motob = Motob()

        self.behaviors = []
        self.add_behavior(Behavior(self, [10000, 0, 0], "drive", 1))
        self.add_behavior(Behavior(self, [30, 0, 0], "stop", 10))
        self.add_behavior(Behavior(self, [0, 0, 0], "turn_around", 9))
        self.add_behavior(Behavior(self, [0, 0, 0], "turn_left", 8))
        self.add_behavior(Behavior(self, [0, 0, 0], "turn_left", 7))
        self.active_behaviors = []

        self.arbitrator = Arbitrator()

    def add_behavior(self, behavior):
        """append a newly-created behavior onto the behaviors list"""
        self.behaviors.append(behavior)

    def add_sensob(self, sensor):
        """append a newly-created sensob onto the sensobs list"""
        self.sensobs.append(sensor)

    def activate_behavior(self, behavior):
        """add an existing behavior onto the active-behaviors list"""
        self.active_behaviors.append(behavior)

    def deactivate_behavior(self, behavior):
        """remove an existing behavior from the active behaviors list"""
        self.active_behaviors.remove(behavior)

    def run_one_timestep(self):
        """constitutes the core BBCON activity"""
        for sensob in self.sensobs:         #Updates all sensobs
            sensob.update()

        for behavior in self.behaviors:     #Update all behaviors
            behavior.update(self.sensobs)

        fav_behavior = self.arbitrator.choose_action(self.active_behaviors)

        self.motob.update(fav_behavior.sense_and_act())

        time.sleep(0.5)


def main():

    m = Motors()
    m.backward()
    m.forward()

    """bbcon = BBCON()
    print("MAIN")
    ZumoButton().wait_for_press()
    while True:
        bbcon.run_one_timestep()"""

if __name__ == "__main__":
    main()
