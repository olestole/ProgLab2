'''Finite State Machine class, with functions'''

class FSM:

    def __init__(self):
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

