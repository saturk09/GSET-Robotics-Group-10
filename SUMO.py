#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor, LightSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55, axle_track=118)
ultrasensor_sensor = UltrasonicSensor(Port.S2)
light_sensor = LightSensor(Port.S3)

def on_white():

ev3.light.on(Color.YELLOW)
while Button.CENTER not in ev3.buttons.pressed():
    wait(10)
ev3.light.on(Color.GREEN)
ev3.speaker.beep()
wait(5000)

if on_white():
    robot.stop()
    robot.drive(-100, 0)
    wait(1000)
    robot.stop()
    continue #will work inside loop





#PUT YOUR CODE HERE  Delete mine

ev3.light.on(Color.RED)
wait(5000)

# robot turns on
# robot spins until it sees the other robot
# once robot sees the other robot, it drives in that direction
# ^^^^ while loop, and add unless it senses it is leaving the field!!! 
#^^^^^^^^^^^^^ NOT LEAVING FIELD IS PRIORITY
# when it senses robot is in 6 inches, it speeds up
# when it senses it is leaving the field, it u turns and moves 6 inches, 
# ^^^then spins until it senses the other robot
# keep moving forward

