#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import CrabRobotLibrary

def run_table(crabot):
	crabot.gyro_reset()
	crabot.back_reset(Direction.COUNTERCLOCKWISE)
		
	# todo: lower the front medium motor so its down

	crabot.front_activate(100, 65, Direction.COUNTERCLOCKWISE)
	crabot.gyro_drive(350, 0, 1270)
	crabot.gyro_drive(40, 0, 385)
	crabot.bw_gyro_drive(-150, 0, -15)
	crabot.gyro_turn(-90, -90)
	crabot.gyro_reset()

	#back into wall and reset

	crabot.bw_gyro_drive(-80, 0, -40)
	crabot.gyro_reset()
	crabot.gyro_drive(500, -0, 1000)
	crabot.gyro_turn(35, Direction.CLOCKWISE)
	crabot.gyro_drive(90, 35, 140)
	wait(1000)

	# flips up boccia ball

	crabot.bw_gyro_drive(-100, 35, -10)
	crabot.front_activate(100, 90, Direction.COUNTERCLOCKWISE)
	crabot.back_activate(200, 250, Direction.CLOCKWISE)
	crabot.bw_gyro_drive(-190, 55, -170)
	wait(1000)
	crabot.back_forever(-800)
	wait(1000)
	crabot.gyro_drive(150, 55, 40)

	# let's dance
	
	crabot.gyro_turn(-85, Direction.COUNTERCLOCKWISE) 
	crabot.front_activate(100, 50, Direction.CLOCKWISE)
	crabot.gyro_drive(250, -50, 600)
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