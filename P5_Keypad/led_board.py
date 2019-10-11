'''Led Board class, with functions'''

class Led_board:

    def setup(self):
        '''Set the proper mode via: GPIO.setmode(GPIO.BCM)'''

    def light_led(self):
        '''Turn on one of the 6 LEDs by making the appropriate combination of input and output declarations,
         and then making the appropriate HIGH / LOW settings on the output pins'''

    def flash_all_leds(self):
        '''Flash all 6 LEDs on and off for k seconds, where k is an argument of the method'''

    def twinkle_all_leds(self):
        '''Turn all LEDs on and off in sequence for k seconds, where k is an argument of the method'''

    def power_up(self):
        '''Led flash when turning on system'''

    def power_down(self):
        '''Led flash when turning off system'''

