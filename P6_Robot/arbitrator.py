

class Arbitrator:

    def __init__(self, i_variable):
        self.instance_variable = i_variable # a pointer to the bbcon

    def choose_action(self):
        """check all of the active behaviors and pick a winner"""

