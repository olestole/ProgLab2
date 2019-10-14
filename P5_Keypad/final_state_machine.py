'''Finite State Machine class, with functions'''

ALL_SYMBOLS = [1, 2, 3, 4, 5, 6, 7, 8, 9, '*', '#']
ALL_DIGITS = [1, 2, 3, 4, 5, 6, 7, 8, 9]

class FSM:

    def __init__(self, k_pad_controller, keypad, l_board):
        self.agent = k_pad_controller
        self.keypad = keypad
        self.led_board = l_board
        self.state =
        self.rule_list = [] #list of rules

    def add_rule(self, rule):
        '''Add rule to rule list'''
        self.rule_list.append(rule)

    def get_next_signal(self):
        '''Query the agent for the next signal'''

    def run_rules(self):
        '''Go through the rule set, in order, applying each rule until one of the rules is fired'''

    def apply_rule(self):
        '''Check whether the conditions of a rule are met'''

    def fire_rule(self):
        '''Use the consequent of a rule to a) set the next state of the FSM, and b) call the appropriate agent action method'''

    def main_loop(self):
        '''Use the consequent of a rule to a) set the next state of the FSM, and b) call the appropriate agent action method'''


class Rule:

    def __init__(self, state1, state2, signal, action):
        self.state1 = state1
        self.state2 = state2
        self.signal = signal
        self.action = action