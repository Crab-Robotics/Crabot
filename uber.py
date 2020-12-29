#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
								 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import CrabRobotLibrary
import run_cheese
import run_treadmill
import run_basketball

crabot = CrabRobotLibrary.Robot("Crabot","Ubertastic")

while True:
	b = EV3Brick.buttons.pressed()
	if Button.CENTER in b:
		print("Running run_treadmill.")
		run_treadmill.go_there(crabot)
		run_treadmill.row_machine(crabot)
		run_treadmill.treadmill(crabot)
		wait(2000)
	elif Button.LEFT in b:
		print("The left button was pressed.")
		crabot.reset_elevator()
		wait(2000)
	elif Button.RIGHT in b:
		print("The right button was pressed.")
		wait(2000)
	elif Button.UP in b:
		#M01, M04, M05, M08 (red or blue blocks)
		print("Running run_basketball.")
		run_basketball.run_table_1(crabot)
		run_basketball.run_table_2(crabot)
		wait(2000)
	elif Button.DOWN in b:
		# M02, M06, M07, M08 (yellow block)
		print("Running run_cheese.")
		run_cheese.run_table(crabot)
		wait(2000)
	else:
		wait(10)

#hewo