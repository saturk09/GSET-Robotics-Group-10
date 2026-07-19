#!/usr/bin/env pybricks-micropython



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
colorSensor = ColorSensor(Port.S1)
while True:
    print(colorSensor.rgb())
    wait(2000)


#will add sensor perhaps in another life
#opticalSensor = UltrasonicSensor(Port.S4)
# drive_speed = 65
# reflection_target = 20
# turn_intensity = .50
# # Write your program here.
# Kp = 3.1
# Kd = 13
# Ki = 0.0007

# i_term = 0
# previous_error = 0
# while True:
#     error = reflection_target - lightSensor.reflection()
#     i_term = i_term + error
#     i_term = max(min(i_term, 100), -100)  # Clamp i_term to prevent windup
#     d_error = error - previous_error
#     previous_error = error

#     bot_corr = Kp * error + Kd * d_error + Ki * i_term

#     if abs(error) > 10:
#         drive_speed = 20
#     elif abs(error) > 5:
#         drive_speed = 40
#     else:
#         drive_speed = 80

#     robot.drive(drive_speed, bot_corr)
#     wait(30)


#obstacle avoidance loop idea
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
