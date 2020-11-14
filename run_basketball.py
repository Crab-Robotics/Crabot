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
	#This will run the basketball mission.
	crabot.gyro_reset()
	crabot.gyro_drive(300, 0, 600)
	crabot.bw_gyro_drive(-100, 0, -50)
	crabot.gyro_turn(45, Direction.CLOCKWISE)
	crabot.gyro_reset()
	crabot.gyro_drive(300, 0, 815)
	crabot.gyro_turn(-80, Direction.COUNTERCLOCKWISE)
	crabot.gyro_reset()
	crabot.gyro_drive(270, 0, 340)
def run_table_2(crabot):
    crabot.front_activate(1000, 7200, Direction.CLOCKWISE)
    wait(500)
    crabot.gyro_reset()
    crabot.bw_gyro_drive(-100,0,-105)
    crabot.front_activate(1000, 7196, Direction.COUNTERCLOCKWISE)
    crabot.gyro_reset()
    crabot.gyro_drive(100,0,100)
    crabot.front_activate(1000, 11180, Direction.CLOCKWISE)
    crabot.front_activate(1000, 1490, Direction.COUNTERCLOCKWISE)
    crabot.gyro_reset()
    crabot.bw_gyro_drive(-100,0,-100)
    crabot.front_activate(1000, 9570, Direction.COUNTERCLOCKWISE)
	
if __name__ == '__main__':
	crabot = CrabRobotLibrary.Robot("Crabot","Competitive")
	run_table_1(crabot)
	run_table_2(crabot)