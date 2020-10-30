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
		try:
			self.gyro = GyroSensor(Port.S2, Direction.CLOCKWISE)
		except:
			self.gyro = None
			print("No Gyro Sensor plugged into Port 2. Cannot run Greyden's Skills. :-(")
			print()
	
	def gyro_angle(self):
		if self.gyro is None:
			return float("nan")
		else:
			return self.gyro.angle()

	def tell_me_about_your_skills(self):
		print("SKILLS - I can read the Gyro Sensor!")
		print("SKILLS - I am able to show you the Gyro angle, see",self.gyro_angle())
		print()

if __name__ == '__main__':
	GreydenSkillBot = Greyden_Skills(None)
	GreydenSkillBot.tell_me_about_your_skills()