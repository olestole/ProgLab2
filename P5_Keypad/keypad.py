'''Keypad class, with functions'''

import RPi.GPIO as GPIO

class Keypad:

    def setup(self):
        '''Set the proper mode via: GPIO.setmode(GPIO.BCM). Also, use GPIO functions to set the row
         pins as outputs and the column pins as inputs'''

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT)
        GPIO.setup(24, GPIO.OUT)
        GPIO.setup(25, GPIO.OUT)

        GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

    def do_polling(self):
    '''Use nested loops (discussed above) to determine the key currently being pressed on the keypad'''

    def get_next_signal(self):
        '''This is the main interface between the agent and the keypad.
         It should initiate repeated calls to do polling until a key press is detected'''
