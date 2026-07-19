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
#will add sensor perhaps in another life
#opticalSensor = UltrasonicSensor(Port.S4)
drive_speed = 65
reflection_target = 20
turn_intensity = .50
victim_count = 0
line_following = True
# Write your program here.
Kp = 3.05
Kd = 13
Ki = 0.0007
i_term = 0
previous_error = 0

while line_following:
    error = reflection_target - lightSensor.reflection()
    i_term = i_term + error
    i_term = max(min(i_term, 100), -100)  # Clamp i_term to prevent windup
    d_error = error - previous_error
    previous_error = error

#     bot_corr = Kp * error + Kd * d_error + Ki * i_term

    if abs(error) > 10:
        drive_speed = 30
    elif abs(error) > 5:
        drive_speed = 50
    else:
        drive_speed = 80
    wait(20)
    
#color detection
while line_following:
    rgb = colorSensor.rgb()
    ev3.screen.print(str(rgb))
    if rgb.b > rgb.r and rgb.b > rgb.g and rgb.b > 55:
        ev3.beep()
        ev3.screen.print(str(victim_count) + "victims found")
        victim_count += 1
        wait(3500) 
    if(rgb.r > rgb.b and rgb.r > rgb.g and rgb.r > 25):
        line_following = False



      

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
