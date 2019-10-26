import sys
import os
#from Help_Classes.camera import Camera
from Help_Classes.imager2 import Imager

class Sensob:

    sensor = None

    def __init__(self, sensor):
        self.sensor = sensor  # Sensor(s)

    def update(self):
        """force the sensob to fetch the relevant sensor value(s) and convert them into the pre-processed sensob value"""
        self.value = self.sensor.update()

    def get_value(self):
        """ Get value from sensor wrapper """
        return self.sensor.get_value()