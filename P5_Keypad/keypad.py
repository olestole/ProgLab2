'''Keypad class, with functions'''

import RPi.GPIO as GPIO
import time

ROWS = [18, 23, 24, 25]
COLUMNS = [17, 27, 22]


class Keypad:

    def __init__(self):
        pass

    def setup(self):

        ''' Set the proper mode via: GPIO.setmode(GPIO.BCM). Also, use GPIO functions to set the row
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

        ''' Use nested loops (discussed above) to determine the key currently being pressed on the keypad'''

        row_col = ()    # Tuple holding the row, col which was pressed

        #print("IN DO_POLLING")

        for row in ROWS:
            GPIO.output(row, GPIO.HIGH)

            for col in COLUMNS:

                if GPIO.input(col) == GPIO.HIGH:

                    """ IMPLEMENT: Avoid noisy inputs from the column pins, it helps to consider the column pin to be 
                    actually high only if repeated measurements (for example, 20 in a row with a 10 millisecond delay 
                    between each reading) all show a high value. You can use the time.sleep() command from Python’s 
                    time package to support this simple (but very important) measure-wait-measure loop."""

                    row_col = (row, col)

            GPIO.output(row, GPIO.LOW)

        return row_col



    def get_next_signal(self):
        '''This is the main interface between the agent and the keypad.
         It should initiate repeated calls to do polling until a key press is detected'''

        pressed = False

        while not pressed:

            #print("IN GET_NEXT_SIGNAL")

            row_col = self.do_polling()
            if row_col:
                print(row_col)
                time.sleep(1)
                #return row_col


def main():
    print("STARTED MAIN FUNC")
    KP = Keypad()
    KP.setup()
    KP.get_next_signal()


if __name__ == "__main__":
    main()

a = (1, 2)
print(not a)