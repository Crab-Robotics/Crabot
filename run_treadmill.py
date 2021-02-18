#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import CrabRobotLibrary

# This program completes the treadmill and the row machine. (Fun fact: this is
# the only run that doesn't do the boccia ball mission.)
#
# How to Use This Function
# -----
# Use the large jig to line up the robot 
# 1. Place the jig against the south wall.
# 2. Leave 4.25000 squares east of the jig.
# 3. Place the robot with the wheel against the llama piece.

def go_there(crabot):
	#resets gyro and drives across the board
	crabot.gyro_reset()
	crabot.gyro_drive(800, 0, 2200)
	crabot.gyro_drive_until_white(400, 0, "left")
	crabot.gyro_drive(200, 0, 165)
	crabot.gyro_turn(-90, Direction.COUNTERCLOCKWISE)
	crabot.bw_gyro_drive(-400, -90, -250)

def treadmill(crabot):
	print("time to get those steps in!")
	crabot.gyro_reset()
	#drives to the treadmill
	crabot.gyro_drive(200, 0, 190) # TODO: 210 works better on some tables
	crabot.gyro_turn(85, Direction.CLOCKWISE)
	crabot.gyro_drive(500, 90, 340) # 370 works better on some tables
	#runs only the left wheel
	while crabot.gyro.angle() > 90:
		crabot.left_wheel.run(-100)
	crabot.left_wheel.stop()
	#drives off the treadmill
	wait(100)
	crabot.right_wheel.run_time(1000, 3000)
	crabot.bw_gyro_drive(-1000, 90, -3000)
	# crabot.gyro_drive(800, -90, 1000)

def row_machine(crabot):
	print("row row row your boat")
	crabot.gyro_reset()
	crabot.front_reset(Direction.COUNTERCLOCKWISE)
	# crabot.bw_gyro_drive(-20, 0, -20)
	#drives to the row machine
	crabot.gyro_drive(200, 0, 420)
	crabot.gyro_turn(49, Direction.CLOCKWISE)
	crabot.gyro_drive(200, 53, 27)
	#pulls the row machine
	crabot.front_activate(100, 220, Direction.CLOCKWISE)
	crabot.front_dog_gear.brake()
	crabot.gyro_turn(0, Direction.COUNTERCLOCKWISE)
	#comes back
	crabot.bw_gyro_drive(-200, 0, -50)
	crabot.front_reset(Direction.COUNTERCLOCKWISE)
	crabot.bw_gyro_drive(-450, 0, -500)

if __name__ == '__main__':
	crabot = CrabRobotLibrary.Robot("Crabot","Competitive")
	go_there(crabot)
	row_machine(crabot)
	treadmill(crabot)
