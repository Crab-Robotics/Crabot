#!/usr/bin/env pybricks-micropython
 
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile 
import CrabRobotLibrary 
# define class robot 
 
class Zac_Skills: 
    def __init__(self, robot): 
        self.robot = robot 
        
    def tell_me_about_your_skills(self): 
        print("Skills - I can dance and run") 
        print('Skills - I can play a song') 
        
    def dance(self, number_of_dances): 
        print("SKILLS - Perform", number_of_dances,"dance moves.")
        y = 1 
        while y <= number_of_dances:
            self.robot.turn(360)
            y = y + 1 
            
    def run(self, number_of_steps):
        print('SKILLS - Run', number_of_steps,'steps.')
        y = 1
        while y <= number_of_steps: 
            self.robot.forward(25)
            y = y + 1
