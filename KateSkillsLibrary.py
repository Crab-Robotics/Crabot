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

    color_sensor_left = ColorSensor(Port.S3)
    color_sensor_right = ColorSensor(Port.S4)
    
    def __init__(self, robot):
        self.robot=robot

    def tell_me_about_your_skills(self):
        print("Check out these skills from Kate:")
        print("Left color sensor RGB reading is",self.color_sensor_left.rgb())
        print("Left color sensor color is",self.color_sensor_left.color())
        print("Right color sensor RGB reading is",self.color_sensor_right.reflected_light_intensity())
        print("Right color sensor color is",self.color_sensor_right.color())
        print("My Gyro is reading",self.robot.gyro.angle())

if __name__ == '__main__':
    Crabot = CrabRobotLibrary.Robot("Crabot","Happy")
	KateSkillBot = Kate_Skills(Crabot)
	KateSkillBot.tell_me_about_your_skills()