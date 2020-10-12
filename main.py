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
import GreydenSkillsLibrary
import KateSkillsLibrary
import ZacSkillsLibrary
import Caleb_Skills_Library

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

Crabot = CrabRobotLibrary.Robot("Crabot","Happy")
Crabot.tell_me_about_yourself()

SkillBot = RichardSkillsLibrary.Richard_Skills(Crabot)
SkillBot.tell_me_about_your_skills()

GreydenSkillBot = GreydenSkillsLibrary.Greyden_Skills(Crabot)
GreydenSkillBot.tell_me_about_your_skills()

KateSkillBot = KateSkillsLibrary.Kate_Skills(Crabot)
KateSkillBot.tell_me_about_your_skills()

ZacSkillBot = ZacSkillsLibrary.Zac_Skills(Crabot)
ZacSkillBot.tell_me_about_your_skills()

CalebSkillBot = Caleb_Skills_Library.Caleb_Skills(Crabot)
CalebSkillBot.tell_me_about_your_skills()

Crabot.move_forward(950)
Crabot.turn(90)
Crabot.move_forward(400)
Crabot.turn(45)
Crabot.move_forward(390)
SkillBot.dance(1)
SkillBot.wiggle(1)
SkillBot.shuffle(1)
SkillBot.wiggle(1)
SkillBot.detect_color()
print()

print('I love dancing')
Crabot.beep(3)
