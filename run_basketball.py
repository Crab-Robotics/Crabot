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
	#This pushes the innovation project out(M01).
	crabot.gyro_reset()
	crabot.gyro_drive(500, 0, 590)
	crabot.brake()
	crabot.bw_gyro_drive(-100, 0, -50)

    #This takes us to the basketball hoop(M05).

	crabot.gyro_turn(45, Direction.CLOCKWISE)
	crabot.gyro_reset()
	crabot.gyro_drive(500, 0, 735)
	crabot.brake()
	crabot.gyro_turn(-85, Direction.COUNTERCLOCKWISE)
	crabot.brake()
	crabot.gyro_reset()
	crabot.gyro_drive(500, 0, 390)
def run_table_2(crabot):

    #this code does the first level of the basketball and lifts the red cube(M05,M08).

    crabot.front_activate(10000, 5766, Direction.CLOCKWISE)
    crabot.front_activate(10000, 1440, Direction.COUNTERCLOCKWISE)
    crabot.gyro_reset()
    crabot.bw_gyro_drive(-100,0,-105)
    crabot.front_activate(10000, 4146, Direction.COUNTERCLOCKWISE)

    #This code does the second level of the basketball(M05).

    crabot.gyro_reset()
    crabot.gyro_drive(300,0,100)
    crabot.front_activate(10000, 11440, Direction.CLOCKWISE)
    crabot.front_activate(10000, 1490, Direction.COUNTERCLOCKWISE)
    crabot.gyro_reset()

    #This code knocks over the bench and returns home(M04).
    
    crabot.bw_gyro_drive(-500,0,-435)
    crabot.gyro_reset()
    crabot.gyro_turn(-27, Direction.COUNTERCLOCKWISE)
    crabot.gyro_reset()
    crabot.gyro_drive(1000, 0, 1350)
    crabot.front_activate(10000, 9230, Direction.COUNTERCLOCKWISE)
    crabot.gyro_reset()
	
if __name__ == '__main__':
	crabot = CrabRobotLibrary.Robot("Crabot","Competitive")
	run_table_1(crabot)
	run_table_2(crabot)
