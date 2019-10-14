'''Finite State Machine class, with functions'''

from keypad_controller import KPC
from keypad import Keypad
from led_board import Led_board
import time





class FSM:

    ALL_SYMBOLS = [1, 2, 3, 4, 5, 6, 7, 8, 9, '*', '#']
    ALL_DIGITS = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self, k_pad_controller, keypad, l_board):
        self.agent = k_pad_controller

        self.keypad = keypad
        self.keypad.setup()

        self.led_board = l_board
        self.led_board.setup()
        
        self.curr_state = "s_init"
        self.rule_list = [] #list of rules
        self.curr_signal = None

    def add_rule(self, rule):
        '''Add rule to rule list'''

        a1 = Rule("s_init", "s_read", 'all_symbols', self.agent.flash_leds())
        a2 = Rule('s_read2', "s_read3", '*', self.agent.flash_leds())

        self.rule_list.append(a1)


    def get_next_signal(self):
        '''Query the agent for the next signal'''
        self.curr_signal = self.keypad.get_next_signal()



    def run_rules(self):
        '''Go through the rule set, in order, applying each rule until one of the rules is fired'''
        for i in self.rule_list:

            if i.state1 == self.curr_state and self.curr_signal in i.legal_signals:
                self.curr_state = i.state2
                i.action()








    def apply_rule(self):
        '''Check whether the conditions of a rule are met'''

    def fire_rule(self):
        '''Use the consequent of a rule to a) set the next state of the FSM, and b) call the appropriate agent action method'''


    def main_loop(self):
        '''Use the consequent of a rule to a) set the next state of the FSM, and b) call the appropriate agent action method'''
        for i in range(10):
            self.keypad.get_next_signal()
            self.run_rules()

            time.sleep(0.5)



class Rule:

    def __init__(self, state1, state2, signal, action):
        self.state1 = state1
        if signal == 'all_symbols':
            self.legal_signals = [1, 2, 3, 4, 5, 6, 7, 8, 9, '*', '#']
        elif signal == 'all_digits':
            self.legal_signals = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        else:
            self.legal_signals = signal

        self.state2 = state2
        self.action = action

def main():
    kpc = KPC()
    keypad = Keypad()
    led_board = Led_board()

    fsm = FSM()
    fsm.main_loop(kpc, keypad, led_board)


if __name__ == "__main__":
    main()