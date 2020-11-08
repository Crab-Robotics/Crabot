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
	crabot.gyro_drive(300, 0, 1300)
	crabot.gyro_drive(40, 0, 365)
	crabot.bw_gyro_drive(-150, 0, -15)
	crabot.gyro_turn(-90, -90)
	crabot.gyro_reset()
	crabot.bw_gyro_drive(-80, 0, -40)
	crabot.gyro_reset()
	crabot.gyro_drive(160, -0, 1000)
	crabot.gyro_turn(25, Direction.CLOCKWISE)
	crabot.gyro_reset()
	crabot.gyro_drive(90, 0, 140)

if __name__ == '__main__':
	crabot = CrabRobotLibrary.Robot("Crabot","Competitive")
	run_table(crabot)
