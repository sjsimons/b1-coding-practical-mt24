class PD_Controller:
    def __init__(self, Kp: float, Kd: float):
        self.Kp = Kp
        self.Kd = Kd
        self.previous_error = 0 # used to calculate derivative error
    
    