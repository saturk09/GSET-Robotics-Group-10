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
ir=InfraredSensor(Port.S4)
rf = UltrasonicSensor(Port.S2)
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

while line_following == False:
    drive_six_inches()
    roomcheck3()
    roomcheck2()
    roomcheck1()
    stop_robots()


def stop_robots():
    robot.stop()
    wait(200)

def turn_robots():
    robot.turn(90)

def read_ir():
    return ir.read("AC")

def drive_six_inches():
    while True:
        robot.drive(100,0)
        if rf.distance() < 152.4:
            stop_robots()

def roomcheck3():
    robot.turn(90)
    wait(100)
    robot.straight(304.8)
    wait(100)
    robot.turn(-90)
    wait(100)
    robot.straight(152.4)
    wait(100)
    for i in range(0, 361):
        if ir.read() == 5:
            robot.drive(100,0)
            wait(5000)
            stop_robots()
            break
        else:
            robot.turn(1)
            wait(30)
            i+=1
    roomcheck2()

def roomcheck2():
    robot.turn(180)
    wait(100)
    robot.straight(152.4)
    wait(100)
    robot.turn(90)
    wait(100)
    robot.straight(304.8)
    robot.straight(285.75)
    wait(100)
    robot.turn(90)
    robot.straight(304.8)
    wait(100)
    for i in range(0, 361):
        if ir.read() == 5:
            robot.drive(100,0)
            wait(5000)
            stop_robots()
            break
        else:
            robot.turn(1)
            wait(30)
            i+=1
    roomcheck1()

def roomcheck1():
    robot.turn(180)
    wait(100)
    robot.straight(304.8)
    wait(100)
    robot.turn(90)
    wait(100)
    robot.straight(254)
    wait(100)
    robot.turn(90)
    robot.straight(152.4)
    wait(100)
    for i in range(0, 361):
        if ir.read() == 5:
            robot.drive(100,0)
            wait(5000)
            stop_robots()
            break
        else:
            robot.turn(1)
            wait(30)
            i+=1
    stop_robots()



      

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
