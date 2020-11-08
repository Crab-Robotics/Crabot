#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import CrabRobotLibrary


# define class robot
class Kate_Skills:

    def tell_me_about_your_skills(self):
        print("Check out these skills from Kate:")
        print("Left color sensor RGB reading is",Crabot.color_sensor_left.rgb())
        print("Left color sensor color is",Crabot.color_sensor_left.color())
        print("Left color sensor reflection is",Crabot.color_sensor_left.reflection())
        print("left color sensor ambient light is",Crabot.color_sensor_left.ambient())
        print("Right color sensor RGB reading is",Crabot.color_sensor_right.rgb())
        print("Right color sensor color is",Crabot.color_sensor_right.color())
        print("Right color sensor reflection is",Crabot.color_sensor_right.reflection())
        print("right color sensor ambient light is",Crabot.color_sensor_right.ambient())
        print("My Gyro is reading",Crabot.gyro.angle())
        Crabot.gyro_reset()
        Crabot.gyro_drive(150,0,750)
        #wait(500)
        Crabot.gyro_drive_reverse(-150,0,-250)

if __name__ == '__main__':
    Crabot = CrabRobotLibrary.Robot("Crabot","Happy")
    KateSkillBot = Kate_Skills(Crabot)
    KateSkillBot.tell_me_about_your_skills()