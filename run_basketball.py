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
	crabot.gyro_drive(300, 0, 780)
	crabot.gyro_turn(-85, Direction.COUNTERCLOCKWISE)
	crabot.gyro_reset()
	crabot.gyro_drive(500, 0, 390)
def run_table_2(crabot):
    #this line of code does the first level of the elevator
    crabot.front_activate(10000, 5766, Direction.CLOCKWISE)
    wait(500)
    crabot.front_activate(10000, 1440, Direction.COUNTERCLOCKWISE)
    crabot.gyro_reset()
    crabot.bw_gyro_drive(-100,0,-105)
    crabot.front_activate(10000, 3966, Direction.COUNTERCLOCKWISE)
    crabot.gyro_reset()
    crabot.gyro_drive(300,0,130)
    crabot.front_activate(10000, 11440, Direction.CLOCKWISE)
    crabot.front_activate(10000, 1490, Direction.COUNTERCLOCKWISE)
    crabot.gyro_reset()
    crabot.bw_gyro_drive(-500,0,-450)
    crabot.gyro_reset()
    crabot.gyro_turn(-27, Direction.COUNTERCLOCKWISE)
    crabot.gyro_reset()
    crabot.gyro_drive(1000, 0, 1300)
    crabot.front_activate(10000, 8000, Direction.COUNTERCLOCKWISE)
    crabot.gyro_reset()
	
if __name__ == '__main__':
	crabot = CrabRobotLibrary.Robot("Crabot","Competitive")
	run_table_1(crabot)
	run_table_2(crabot)