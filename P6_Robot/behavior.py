"""It violates the fundamental principles of BBR to design behaviors
that communicate directly with one another.
All interaction occurs indirectly via either the arbitrator
or via information posted by one behavior
(in the bbcon) and read by a second behavior (from the bbcon) 3
One important condition for receiving a passing mark on this
project is that your group’s code obey’s this simple,
 yet extremely important, principle.
"""


class Behavior:
    """ a modular unit designed to analyze a subset
        of the sensory information as the basis for determining a motor request.
        Behaviors operate in avacuum in the sense that they have no knowledge of
        or direct connection to other behaviors.
    """

    def __init__(
            self,
            bbcon,
            sensor_limits,
            #sensobs,
            motor_recommendations,
            priority,
            active_flag=False):
            #halt_request=False):
        self.bbcon = bbcon  # pointer to the controller that uses this behavior.,
        # a list of all sensobs that this behavior uses.
        self.sensor_limits = sensor_limits
        # list of recommendations, 1/motob, that this behavior provides to the
        # arbitrator.
        self.motor_recommendations = motor_recommendations  # a list of recommendations
        self.active_flag = active_flag  # is behavior active or not
        #self.halt_request = halt_request  # request the robot to completely halt activity
        # a static, pre-defined value indicating the importance of this
        # behavior
        self.priority = priority
        # a real number in the range [0, 1] indicating the degree to which
        # current conditions warrant the performance of this behavior.
        #self.match_degree = match_degree
        # arbitrator uses as the basis for selecting the winning behavior for a
        # timestep.
        #self.weigth = priority * match_degree

    def consider_deactivation(self):
        """ whenever a behavior is active, it should test whether it should deactivate."""
        if self.active_flag:
            sensor_count = 0
            for sensor in self.sensobs:
                if sensor.get_value() > self.sensor_limits[0]:
                    self.active_flag = False
                    self.bbcon.deactivate_behavior(self)
                    break
                sensor_count += 1

    def consider_activation(self):
        """whenever a behavior is inactive, it should test whether it should activate."""
        if not self.active_flag:
            sensor_count = 0
            for sensor in self.sensobs:

                print("sensor", sensor)
                print("sensor values", sensor.get_value())
                print("ssensor_lim", self.sensor_limits[0])
                if sensor.get_value() < self.sensor_limits[0]:
                    self.active_flag = True
                    self.bbcon.activate_behavior(self)
                    break
                sensor_count += 1

    def update(self, sensobs):
        """the main interface between the bbcon and the behavior
        implement test s for becoming active or inactive"""
        self.sensobs = sensobs
        self.consider_activation()
        self.consider_deactivation()

    def sense_and_act(self):
        """the core computations performed by the behavior that use sensob readings
        to produce motor recommendations (and halt requests)."""
        return self.motor_recommendations
