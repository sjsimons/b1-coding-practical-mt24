class PD_Controller:
    """Simple PD controller implementation for uuv submarine control scenario with adjustable gain"""
    def __init__(self, Kp: float, Kd: float):
        self.Kp = Kp
        self.Kd = Kd
        self.previous_error = 0 # used to calculate derivative error
    
    def response(self, observation: float, reference: float):
        error = reference - observation
        action = self.Kp * error + self.Kd * (error - self.previous_error)

        self.previous_error = error
        return action