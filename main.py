#!/usr/bin/env pybricks-micropython

from ast import While

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.nxtdevices import (LightSensor, SoundSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55, axle_track=118)
lightSensor = LightSensor(Port.S3)

#opticalSensor = UltrasonicSensor(Port.S4)

drive_speed = 500
#robot.straight(1000)

# Write your program here.

while True:
    absorbance = lightSensor.reflection()
    ev3.speaker.bep()
    ev3.speaker.say("Absorbance is " + str(absorbance))
    wait(2000)
#line following loop
    if absorbance < 50:
        robot.drive(drive_speed, 30)
    else:
        robot.drive(drive_speed, -30)

#obstacle avoidance loop
#  while True:
#     distance = opticalSensor.distance()
#     if distance < 200:
#         robot.stop()
#         ev3.speaker.say("Obstacle detected")
#         wait(1000)
#         robot.straight(-100)
#         robot.turn(90)
#         robot.straight(100)
#     else:
#         robot.drive(drive_speed, 0)
