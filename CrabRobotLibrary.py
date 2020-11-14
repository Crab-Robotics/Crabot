#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
								 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Define Class Robot

class Robot:
	brick = EV3Brick()
	left_wheel = Motor(Port.A)
	right_wheel = Motor(Port.D)
	front_dog_gear = Motor(Port.C)
	back_dog_gear = Motor(Port.B)
	right_color = ColorSensor(Port.4)
	left_color = ColorSensor(Port.1)
	gyro = GyroSensor(Port.S2, Direction.COUNTERCLOCKWISE)
	wheel_diameter = 95
	axle_track = 120
	robot = DriveBase(left_wheel, right_wheel, wheel_diameter, axle_track)

	def __init__(self, name, mood):
		# self.robot.settings(0, 0, 100, 50)
		self.name = name
		self.mood = mood

	def tell_me_about_yourself(self):
		print("The robot's name is " + self.name + ".")
		print("This robot is " + self.mood + ".")
		print("Wheel diameter is", self.wheel_diameter, ".")
		print("Axle Track is", self.axle_track, ".")
		print()

	def move_forward(self, distance_mm):
		print("Move forward", distance_mm, ".")
		self.robot.straight(-distance_mm)
	  
	def turn(self, angle):
		print("Turn", angle, "degrees.")
		self.robot.turn(angle)

	def gyro_reset(self):
		self.gyro.reset_angle(0)
		while self.gyro.angle() != 0:
			self.gyro.reset_angle(0)
			wait(50)

	def gyro_turn(self, degrees, direction):
		print("start: " + str(self.gyro.angle()))
		self.robot.stop()
		speed = 150
		if direction == Direction.CLOCKWISE:
			self.left_wheel.run(speed)
			self.right_wheel.run(-speed)
			while self.gyro.angle() < degrees:
				wait(10)
		else:
			self.left_wheel.run(-speed)
			self.right_wheel.run(speed)
			while self.gyro.angle() > degrees:
				wait(10)
		
		self.left_wheel.stop(Stop.BRAKE)
		self.right_wheel.stop(Stop.BRAKE)
		print("stop:  " + str(self.gyro.angle()))

	def gyro_drive(self, speed, heading, distance):
		self.robot.stop()
		self.robot.reset()
		actual_distance = 0
		while actual_distance < distance:
			correction = self.gyro.angle() * -10
			self.robot.drive(speed, correction)
			wait(10)
			actual_distance = self.robot.distance()

	def bw_gyro_drive(self, speed, heading, distance):
		self.robot.stop()
		self.robot.reset()
		actual_distance = 0
		while actual_distance > distance:
			correction = self.gyro.angle() * -10
			self.robot.drive(speed, correction)
			wait(10)
			actual_distance = self.robot.distance()

	def beep(self, number_of_beeps):
		print("Beep",number_of_beeps,"times.")
		x = 1
		while x <= number_of_beeps: 
			self.brick.speaker.beep()
			wait(30)
			x = x + 1

	def move_backwards(self, distance_mm):
		print("Move backwards",distance_mm,".")
		self.robot.straight(distance_mm)

if __name__ == '__main__':
	Crabot = Robot("Crabot Test","Testy")
	Crabot.tell_me_about_yourself()
