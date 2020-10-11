#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
								 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Define Class Robot
class Greyden_Skills:
	def __init__(self, robot):
		self.robot = robot

	def tell_me_about_your_skills(self):
		print("SKILLS - I can read the Gyro Sensor!")
		print("SKILLS - I am able to show you the Gyro angle, see",self.robot.gyro.angle())
		print()