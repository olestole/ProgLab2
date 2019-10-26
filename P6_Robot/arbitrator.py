""" Finds the most important behavior by weigth"""


class Arbitrator:
    """Decides at each timestep: which behavior wins
    and thus gets its motor recommendations transferred to the agent's motobs"""

    def __init__(self, active_behaviors):
        self.active_behaviors = active_behaviors

    def choose_action(self): #stochastic solution
        """check all of the active behaviors and return a winner with highest weight
            returns motor_recommendations and halt request for winner behavior"""
        highest_weight = 0
        highest_behavior = None
        for behavior in self.active_behaviors:
            if behavior.weigth > highest_weight:
                highest_behavior = behavior
        return highest_behavior.motor_recommendations, highest_behavior.halt_request


