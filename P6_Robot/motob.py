"""The motor object (motob) manifests an interface between a behavior and one or more motors"""

class Motob:

    def __init__(self, value):
        self.motors = [] #list of the motors whose settings will be determined by the motob
        self.value = value #a holder of the most recent motor recommendation sent to the motob

    def update(self):
        """receive a new motor recommendation, load it into the value slot, and operationalize it"""

    def operationalize(self):
        """convert a motor recommendation into one or more motor settings, which are sent to the corresponding motor(s)"""

