#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Define Class Robot
# This class defines all of the functions and variables needed to run
# the robot. We use this class in other programs.

class Robot:
	brick = EV3Brick()
	left_wheel = Motor(Port.A)
	right_wheel = Motor(Port.D)
	front_dog_gear = Motor(Port.B)
	back_dog_gear = Motor(Port.C)
	#right_color = ColorSensor(Port.S4)
	left_color = ColorSensor(Port.S1)
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
	
	# This function makes sure all of the motors spin freely.
	def coast(self):
		self.front_dog_gear.stop()
		self.back_dog_gear.stop()
		self.left_wheel.stop()
		self.right_wheel.stop()
	
	# This function activates the front attachment.
	def front_activate(self, speed, rotation_angle, direction = Direction.CLOCKWISE):
		print("Activating front motor")
		if direction == Direction.CLOCKWISE:
			self.front_dog_gear.run_angle(speed, rotation_angle)
		elif direction == Direction.COUNTERCLOCKWISE:
			self.front_dog_gear.run_angle(-speed, rotation_angle)
	
	# This function resets the front attachment.
	def front_reset(self, direction = Direction.CLOCKWISE):
		if direction == Direction.CLOCKWISE:
			self.front_dog_gear.run_time(500, 1000)
		elif direction == Direction.COUNTERCLOCKWISE:
			self.front_dog_gear.run_time(-500, 1000)

	# This function makes the front attachment activate forever.
	def front_forever(self, speed, direction = Direction.CLOCKWISE):
		print("Activating front motor")
		if direction == Direction.CLOCKWISE:
			self.front_dog_gear.run(speed)
		elif direction == Direction.COUNTERCLOCKWISE:
			self.front_dog_gear.run(-speed)
	
	# This function resets the back attachment.
	def back_reset(self, direction = Direction.CLOCKWISE):
		if direction == Direction.CLOCKWISE:
			self.back_dog_gear.run_time(500, 1000)
		elif direction == Direction.COUNTERCLOCKWISE:
			self.back_dog_gear.run_time(-500, 1000)

	# This function activates the back attachment.
	def back_activate(self, speed, rotation_angle, direction = Direction.CLOCKWISE):
		print("Activating back motor")
		if direction == Direction.CLOCKWISE:
			self.back_dog_gear.run_angle(speed, rotation_angle)
		elif direction == Direction.COUNTERCLOCKWISE:
			self.back_dog_gear.run_angle(-speed, rotation_angle)

	# This function makes the back attachment activate forever.
	def back_forever(self, speed, direction = Direction.CLOCKWISE):
		print("Activating back motor")
		if direction == Direction.CLOCKWISE:
			self.back_dog_gear.run(speed)
		elif direction == Direction.COUNTERCLOCKWISE:
			self.back_dog_gear.run(-speed)
	
	# This function locks the back attachment.
	def back_brake(self):
		print("Stopping back motor")
		self.back_dog_gear.brake()

	# This function resets both attachments at the same time.
	def reset_attachments(self):
		print("Resetting attachments")
		self.front_forever(1000, Direction.COUNTERCLOCKWISE)
		self.back_forever(1000, Direction.COUNTERCLOCKWISE)
		wait(500)
		self.front_dog_gear.brake()
		self.back_dog_gear.brake()

	# This function automatically resets the elevator attachment
	# (because we are too lazy to do it ourselves by hand).
	def reset_elevator(self):
		self.front_dog_gear.run_until_stalled(-10000, Stop.COAST)

	# This function makes the robot drive straight without using
	# the gyro.
	def move_forward(self, distance_mm):
		print("Move forward", distance_mm, ".")
		self.robot.straight(-distance_mm)

	# This function turns the robot without using the gyro.
	def turn(self, angle):
		print("Turn", angle, "degrees.")
		self.robot.turn(angle)

	# This function locks the wheels.
	def brake(self):
		self.left_wheel.brake()
		self.right_wheel.brake()

	# This function resets the gyro's angle value to 0.
	def gyro_reset(self):
		self.gyro.reset_angle(0)
		while self.gyro.angle() != 0:
			self.gyro.reset_angle(0)
			wait(50)

	# This function causes the robot to turn until the gyro reads a
	# certain angle.
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

	# This function makes the robot drive straight using the gyro
	# sensor for a given distance.
	def gyro_drive(self, speed, heading, distance):
		self.robot.stop()
		self.robot.reset()
		actual_distance = 0
		while actual_distance < distance:
			adjusted_angle =  self.gyro.angle() - heading
			correction = adjusted_angle * -10
			self.robot.drive(speed, correction)
			wait(10)
			actual_distance = self.robot.distance()
		self.robot.stop()

	# This function makes the robot drive straight using the gyro
	# sensor until the color sensor detects white.
	def gyro_drive_until_white(self, speed, heading, side):
		self.robot.stop()
		self.robot.reset()
		sensor = self.left_color
		if side == "left":
			sensor = self.left_color
		while sensor.reflection() < 50:
			adjusted_angle =  self.gyro.angle() - heading
			correction = adjusted_angle * -10
			self.robot.drive(speed, correction)
		self.robot.stop()

	# This function makes the robot drive backwards using the gyro
	# sensor for a given distance.
	def bw_gyro_drive(self, speed, heading, distance):
		self.robot.stop()
		self.robot.reset()
		actual_distance = 0
		while actual_distance > distance:
			adjusted_angle =  self.gyro.angle() - heading
			correction = adjusted_angle * -10
			self.robot.drive(speed, correction)
			wait(10)
			actual_distance = self.robot.distance()
		self.robot.stop()

	# This function checks to see if the robot is right-side-up. 
	# If not, it will beep and complain.
	# But, it can only tell if it falls to the left or right,
	# it can't tell if it has fallen forward or backward.
	def fall_check(self):
		fall_gyro = GyroSensor(Port.S4, Direction.CLOCKWISE)
		while True:
			real_angle = fall_gyro.angle()
			if real_angle > 45 or real_angle < -45:
				self.brick.speaker.beep()
			else:
				wait(30)
			print(real_angle)

	# This function beeps.
	def beep(self, number_of_beeps):
		print("Beep",number_of_beeps,"times.")
		x = 1
		while x <= number_of_beeps: 
			self.brick.speaker.beep()
			wait(30)
			x = x + 1

	# This function makes the robot drive backwards without using the
	# gyro sensor.
	def move_backwards(self, distance_mm):
		print("Move backwards",distance_mm,".")
		self.robot.straight(distance_mm)

if __name__ == '__main__':
	Crabot = Robot("Crabot Test","Testy")
	Crabot.tell_me_about_yourself()
