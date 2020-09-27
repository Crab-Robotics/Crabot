#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
								 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

#def mission1():
	# do mission 1
	# gyro-drive and stuff
	# mission 1 is complete

while True:
	b = EV3Brick.buttons.pressed()
	if Button.CENTER in b:
		print("The center button was pressed.")
		wait(2000)
	elif Button.LEFT in b:
		print("The left button was pressed.")
		wait(2000)
	elif Button.RIGHT in b:
		print("The right button was pressed.")
		wait(2000)
	elif Button.UP in b:
		print("The top button was pressed.")
		wait(2000)
	elif Button.DOWN in b:
		print("The bottom button was pressed.")
		wait(2000)
	else:
		wait(10)
	