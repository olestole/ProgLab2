'''Led Board class, with functions'''

import RPi.GPIO as GPIO
from time import sleep

"""
        GPIO.setup(13, GPIO.IN)  = pin0
        GPIO.setup(20, GPIO.OUT) = pin1
        GPIO.setup(21, GPIO.OUT) = pin2
"""

class Led_board:

    pins = [13, 20, 21]

    pin_led_states = [
        [1, 0, -1],  # A
        [0, 1, -1],  # B
        [-1, 1, 0],  # C
        [-1, 0, 1],  # D
        [1, -1, 0],  # E
        [0, -1, 1]  # F
    ]

    def setup(self):
        '''Set the proper mode via: GPIO.setmode(GPIO.BCM)'''
        GPIO.setmode(GPIO.BCM)

    def set_pin(self, pin_index, pin_state):
        if pin_state == -1:
            GPIO.setup(self.pins[pin_index], GPIO.IN)
        else:
            GPIO.setup(self.pins[pin_index], GPIO.OUT)
            GPIO.output(self.pins[pin_index], pin_state)

    def light_led(self, led_number):
        '''Turn on one of the 6 LEDs by making the appropriate combination of input and output declarations,
         and then making the appropriate HIGH / LOW settings on the output pins'''
        for pin_index, pin_state in enumerate(self.pin_led_states[led_number]):
            self.set_pin(pin_index, pin_state)

    def flash_all_leds(self):
        '''Flash all 6 LEDs on and off for k seconds, where k is an argument of the method'''

    def twinkle_all_leds(self):
        '''Turn all LEDs on and off in sequence for k seconds, where k is an argument of the method'''


    def power_up(self):
        '''Led flash when turning on system'''
        self.light_led(4)


    def power_down(self):
        '''Led flash when turning off system'''
        self.light_led(5)


def main():
    print("START")
    board = Led_board()
    board.setup()
    #board.power_up()
    #sleep(5)
    #board.power_down()
    board.light_led(0)
    board.light_led(1)
    board.light_led(2)
    board.light_led(3)
    board.light_led(4)
    board.light_led(5)

if __name__ == '__main__':
    main()




