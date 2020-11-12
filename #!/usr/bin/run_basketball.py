#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import CrabRobotLibrary

def run_table_1(crabot):
	front_dog_gear = Motor(Port.C)
	crabot.gyro_reset()
	crabot.gyro_drive(300, 0, 600)
	crabot.bw_gyro_drive(-300, 0, -50)
	crabot.gyro_turn(45, Direction.CLOCKWISE)
	crabot.gyro_reset()
	crabot.gyro_drive(300, 0, 805)
	crabot.gyro_turn(-88, -88)
	crabot.gyro_reset()
	crabot.gyro_drive(250, 0, 260)
	
	

if __name__ == '__main__':
	crabot = CrabRobotLibrary.Robot("Crabot","Competitive")
	run_table_1(crabot)
