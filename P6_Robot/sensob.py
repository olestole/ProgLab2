import sys
import os
from Help_Classes.camera import Camera
from Help_Classes.imager2 import Imager

class Sensob:

    sensor = None
    value = None

    def __init__(self, sensor):
        self.sensor = sensor  # Sensor(s)

    def update(self):
        """force the sensob to fetch the relevant sensor value(s) and convert them into the pre-processed sensob value"""
        self.value = self.sensor.sensor_get_value()

    def get_value(self):
        """ Get value from sensor wrapper """
        return self.value
        
c = Camera()
i = Imager()
print(i)