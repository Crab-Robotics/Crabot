#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
								 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import CrabRobotLibrary
import RichardSkillsLibrary

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

crabot = CrabRobotLibrary.Robot("Crabot","Happy")
crabot.tell_me_about_yourself()

crabot.gyro_reset()
crabot.gyro_turn(90, Direction.CLOCKWISE)
crabot.gyro_turn(180, Direction.CLOCKWISE)
crabot.gyro_turn(350, Direction.CLOCKWISE)