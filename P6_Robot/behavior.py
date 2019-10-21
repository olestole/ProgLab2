"""It violates the fundamental principles of BBR to design behaviors that communicate directly with one another.
All interaction occurs indirectly via either the arbitrator or via information posted by one behavior
(in the bbcon) and read by a second behavior (from the bbcon) 3
One important condition for receiving a passing mark on this project is that your group’s code obey’s this simple,
 yet extremely important, principle.
"""

Class Behavior:

    def __init__(self, bbcon, sensobs, motor_recommendations, priority, match_degree,halt_request=False, active_flag=False):
        self.bbcon = bbcon #pointer to the controller that uses this behavior.,
        self.sensobs = [] #a list of all sensobs that this behavior uses.
        self.motor_recommendations = [] # list of recommendations, 1/motob, that this behavior provides to the arbitrator.
        self.active_flag = active_flag #is behavior active or not
        self.halt_request = halt_request # request the robot to completely halt activity
        self.priority = priority #a static, pre-defined value indicating the importance of this behavior
        self.match_degree = match_degree # a real number in the range [0, 1] indicating the degree to which current conditions warrant the performance of this behavior.
        self.weigth = priority*match_degree #arbitrator uses as the basis for selecting the winning behavior for a timestep.

