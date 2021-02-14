#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
								 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import CrabRobotLibrary

def run_table_3(crabot):
	#drives to the big boccia ball area
	crabot.gyro_reset()
	crabot.gyro_drive(500, 0, 130)
	crabot.gyro_turn(48, Direction.CLOCKWISE)
	crabot.gyro_drive(10000, 48, 1650)
	crabot.brake()
	#Dumps out the cubes
	crabot.front_activate(10000, 3600, Direction.CLOCKWISE)
	#comes back to home
	crabot.bw_gyro_drive(-10000, 48, -1780)
	crabot.brake()
	crabot.reset_elevator()

if __name__ == '__main__':
	crabot = CrabRobotLibrary.Robot('Crabot','Competitive')
	run_table_3(crabot)
