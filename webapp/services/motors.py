from gpiozero import Motor

class Motors:

    def __init__(self):
        self.motor = Motor(17,18)

    def move_forward(self):
        self.motor.forward()

    def move_backward(self):
        self.motor.backward()

    def stop_motor(self):
        self.motor.stop()
