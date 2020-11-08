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

print("Press a button to load a library:\nCenter = Richard's Library\nRight = Greyden's Library\nLeft = Kate's Library\nUp = Zac's Library\nDown = Caleb's Library")
while True:
    b = EV3Brick.buttons.pressed()
    if Button.CENTER in b:
        SkillBot = RichardSkillsLibrary.Richard_Skills(Crabot)
        SkillBot.tell_me_about_your_skills()
        SkillBot.dance(1)
        SkillBot.wiggle(1)
        SkillBot.shuffle(1)
        SkillBot.wiggle(1)
        SkillBot.detect_color()
        wait(2000)
        break
    elif Button.RIGHT in b:
        GreydenSkillBot = GreydenSkillsLibrary.Greyden_Skills(Crabot)
        GreydenSkillBot.tell_me_about_your_skills()
        wait(2000)
        break
    elif Button.LEFT in b:
        KateSkillBot = KateSkillsLibrary.Kate_Skills(Crabot)
        KateSkillBot.tell_me_about_your_skills()
        wait(2000)
        break
    elif Button.UP in b:
        ZacSkillBot = ZacSkillsLibrary.Zac_Skills(Crabot)
        ZacSkillBot.tell_me_about_your_skills()
        wait(2000)
        break
    elif Button.DOWN in b:
        CalebSkillBot = Caleb_Skills_Library.Caleb_Skills(Crabot)
        CalebSkillBot.tell_me_about_your_skills()
        wait(2000)
        break
    else:
        wait(10)


# Crabot.move_forward(950)
# Crabot.turn(90)
# Crabot.move_forward(400)
# Crabot.turn(45)
# Crabot.move_forward(390)

print()

print('I love dancing')
print("I am Crabbot, I like cheese!")
Crabot.beep(3)
