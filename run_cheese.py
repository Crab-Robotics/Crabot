#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import CrabRobotLibrary

# How to Use This Function
# -----
# Use the small jig to line up the robot 
# 1. Place the jig against the south wall.
# 2. Leave 4.25000 squares east of the jig.
# 3. Place the robot with the wheel against the llama piece.

def run_table(crabot):
	crabot.gyro_reset()
	# todo: create front_and_back_reset function to reduce time
	crabot.back_reset(Direction.COUNTERCLOCKWISE)
	crabot.front_reset(Direction.COUNTERCLOCKWISE)
		
	# todo: lower the front medium motor so its down

	crabot.front_activate(200, 195, Direction.CLOCKWISE)
	crabot.gyro_drive(350, 0, 1180)
	crabot.gyro_drive(40, 0, 385)
	crabot.bw_gyro_drive(-150, 0, -15)
	crabot.gyro_turn(-90, -90)
	crabot.gyro_reset()

	#back into wall and reset

	crabot.bw_gyro_drive(-120, 0, -80)
	crabot.gyro_reset()
	crabot.gyro_drive(750, -0, 1000)
	crabot.gyro_turn(35, Direction.CLOCKWISE)
	crabot.gyro_drive(90, 40, 130)
	wait(100)

	# flips up boccia ball

	crabot.bw_gyro_drive(-100, 40, -35)
	crabot.front_activate(100, 90, Direction.COUNTERCLOCKWISE)
	crabot.back_activate(200, 250, Direction.CLOCKWISE)
	crabot.bw_gyro_drive(-190, 55, -170)
	wait(100)
	crabot.back_forever(-1000)
	wait(100)
	crabot.gyro_drive(150, 55, 40)

	# let's dance
	
	crabot.gyro_turn(-50, Direction.COUNTERCLOCKWISE) 
	crabot.front_forever(1000, Direction.COUNTERCLOCKWISE)
	crabot.gyro_drive(500, -50, 600)
	crabot.front_dog_gear.stop()
	crabot.gyro_reset()
	while True:
		crabot.gyro_drive(90, 0, 100)
		crabot.bw_gyro_drive(-90, 0, -100)
		wait(200)
		crabot.gyro_turn(45, Direction.CLOCKWISE)
		crabot.gyro_reset()
		wait(200)
		crabot.gyro_turn(-45, Direction.COUNTERCLOCKWISE)
		crabot.gyro_reset()
		wait(200)
		crabot.gyro_turn(-45, Direction.COUNTERCLOCKWISE)
		crabot.gyro_reset()
		wait(200)
		crabot.gyro_turn(45, Direction.CLOCKWISE)
		crabot.gyro_reset()
		wait(200)
		crabot.front_activate(-100, -100, Direction.COUNTERCLOCKWISE)
		crabot.front_activate(100, 100, Direction.CLOCKWISE)
if __name__ == '__main__':
	crabot = CrabRobotLibrary.Robot("Crabot","Competitive")
	run_table(crabot)