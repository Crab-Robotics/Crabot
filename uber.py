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
import run_cube

# This program is our main control loop. It starts an infinite loop (that means
# it runs forever) that waits for a button press. Then, depending on which button
# is pressed, it runs a different program.
# -----
# UP: run_basketball
# RIGHT: run_cube
# DOWN: run_treadmill
# LEFT: run_cheese
# CENTER: reset_elevator

crabot = CrabRobotLibrary.Robot("Crabot","Ubertastic")

crabot.coast()
while True:
	b = EV3Brick.buttons.pressed()
	if Button.CENTER in b:
		print("Resetting elevator.")
		crabot.reset_elevator()
		crabot.coast()
		wait(2000)
	elif Button.LEFT in b:
		# M02, M06, M07, M08 (yellow block) - run_cheese
		print("Running run_cheese.")
		run_cheese.run_table(crabot)
		crabot.coast()
		wait(2000)
	elif Button.RIGHT in b:
		# M08 (All other cubes) - run_cube
		print("Running run_cube.")
		run_cube.run_table_3(crabot)
		crabot.coast()
		wait(2000)
	elif Button.UP in b:
		#M01, M04, M05, M08 (red or blue blocks) -  run_basketball
		print("Running run_basketball.")
		run_basketball.run_table_1(crabot)
		run_basketball.run_table_2(crabot)
		crabot.coast()
		wait(2000)
	elif Button.DOWN in b:
		# M11, M12 - run_treadmill
		print("Running run_treadmill.")
		run_treadmill.go_there(crabot)
		run_treadmill.row_machine(crabot)
		run_treadmill.treadmill(crabot)
		crabot.coast()
		wait(2000)
	else:
		wait(10)
