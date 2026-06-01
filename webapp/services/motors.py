from gpiozero import Motor
from time import sleep

class Motors:

    def __init__(self,forward,backward):
        self.motor = Motor(forward,backward)

    def move_forward(self):
        self.motor.forward(1)
        sleep(5)
        self.motor.stop()

    def move_backward(self):
        self.motor.backward(1)
        sleep(2)
        self.motor.stop()

    def stop_motor(self):
        self.motor.stop()
