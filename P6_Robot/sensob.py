import sys
import os
from Help_Classes.camera import Camera
from Help_Classes.imager2 import Imager

class Sensob:

    def __init__(self):
        self.sensor = None  # Sensor(s)
        self.value = None   #Sensor(s) value

    def update(self):
        """force the sensob to fetch the relevant sensor value(s) and convert them into the pre-processed sensob value"""
        
    def get_value(self):
        """ Get value from sensor wrapper """
        
c = Camera()
i = Imager()
print(c)