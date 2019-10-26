"""The motor object (motob) manifests an interface between a behavior and one or more motors"""

from Help_Classes.motors import Motors

class Motob:

    def __init__(self):
        self.motor = Motors()
        self.value = ""

    def update(self, motor_recommendations):
        """receive a new motor recommendation, load it into the value slot, and operationalize it"""
        self.value = motor_recommendations
        self.operationalize()

    def operationalize(self):
        """convert a motor recommendation into one or more motor settings, which are sent to the corresponding motor(s)"""
        print("motob value: ", self.value)
        if(self.value == "drive"):
            self.motor.forward(.4, 0.2)
        elif(self.value == "stop"):
            self.motor.stop()
        elif(self.value == "turnaround"):
            self.motor.left(.4, 4)
        elif(self.value == "turn_left"):
            self.motor.left()
        elif(self.value == "turn_right"):
            self.motor.right()
            