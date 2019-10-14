'''Keypad Controller class, with functions'''
from keypad import Keypad
from led_board import Led_board

class KPC:

    def __init__(self, p_keypad, p_ledboard, p_name, password):
        self.pointer_keypad = p_keypad
        self.pointer_ledboard = p_ledboard
        '''a few simple strings or arrays for holding important sequences of keystrokes, such as a passcode-buffer for all numbers in an ongoing password-entry attempt'''
        self.password_buffer = ""
        self.password = password
        self.pathname = p_name  # the complete pathname to the file holding the KPC’s password
        self.override_signal = ""
        '''slotsforholdingtheLEDid(Lid)andlightingduration(Ldur)–bothenteredviathekeypad – so that it can initiate the action of turning a specific LED on for a specific length of time'''

    def init_passcode_entry(self):
        '''Clear the passcode-buffer and initiate a ”power up” lighting sequence on the LED Board. This should be done when the user first presses the keypad'''
        self.password_buffer = ""
        self.pointer_ledboard.power_up()

    def get_next_signal(self):
        '''Return the override-signal, if it is non-blank; otherwise query the keypad for the next pressed key'''
        if self.override_signal:
            return self.override_signal
        else:
            self.pointer_keypad.get_next_signal()

    def verify_login(self):
        '''Check that the password just entered via the keypad matches that in the pass- word file.
        Store the result (Y or N) in the override-signal. Also, this should call the LED Board to initiate the appropriate
         lighting pattern for login success or failure'''
        if self.password_buffer == self.password:
            self.twinkle_leds(3)
            self.override_signal = "Y"
        else:
            self.flash_leds(3)
            self.override_signal = "N"

    def validate_passcode_change(self, new_passw):
        '''Check that the new password is legal. If so, write the new pass- word in the password file.
        A legal password should be at least 4 digits long and should contain no symbols other than the digits 0-9.
        As in verify login, this should use the LED Board to signal success or failure in changing the password'''

    def light_one_led(self):
        '''Using values stored in the Lid and Ldur slots, call the LED Board and request that LED # Lid be turned on for Ldur seconds'''

    def flash_leds(self, k):
        '''Call the LED Board and request the flashing of all LEDs'''
        self.pointer_ledboard.flash_all_leds(k)

    def twinkle_leds(self, k):
        '''Call the LED Board and request the twinkling of all LEDs'''
        self.pointer_ledboard.twinkle_all_leds(k)

    def exit_action(self):
        '''Call the LED Board to initiate the ”power down” lighting sequence'''
        self.pointer_ledboard.power_down()


def main():
    print("START")
    qpad = Keypad()
    qpad.setup()
    ledboard = Led_board()
    ledboard.setup()
    kpc = KPC(qpad, ledboard, "filepath", "1234")
    kpc.flash_leds(5)




if __name__ == '__main__':
    main()

