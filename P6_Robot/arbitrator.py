""" Validate  """


class Arbitrator:

    instance_variable = None   # a pointer to the bbcon

    def __init__(self, i_variable):
        self.instance_variable = i_variable

    def choose_action(self, active_behaviors):
        """check all of the active behaviors and return a winner"""

