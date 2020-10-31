#!/usr/bin/env pybricks-micropython 
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import CrabRobotLibrary
#define class robot 
 
class Zac_Skills: 
    def __init__(self, robot): 
        self.robot = robot 
    
    def tell_me_about_your_skills(self): 
        print("Skills - I can dance, run, and follow a line") 
        print('Skills - I can play a song') 
        
    def dance(self, number_of_dances): 
        print("SKILLS - Perform", number_of_dances,"dance moves.") 
        y = 1 
        while y <= number_of_dances: 
            self.robot.forward(2) 
            self.robot.backword(2) 
            self.robot.turn(270) 
            self.robot.forward(2) 
            self.robot.backword(2) 
            self.robot.turn(270) 
            y = y + 1 
        
    def run(self, number_of_steps): 
        print('SKILLS - Run', number_of_steps,'steps.') 
        y = 1 
        while y <= number_of_steps: 
            self.robot.forward(25) 
            y = y + 1 
            
    def follow(self, number_of_seconds): 
        print('SKILLS - Follow the line for', number_of_seconds,'seconds') 
        y = 1 
        while y <= number_of_seconds: 
            left_motor = Motor(Port.A) 
            right_motor = Motor(Port.D) 
            
        color_sensor_left = ColorSensor(Port.S3) 
        color_sensor_right = ColorSensor(Port.S4) 
            
        robot = DriveBase(left_motor, right_motor, wheel_diameteR, axle_track) 
        BLACK = 9 
        WHITE = 85 
            
        threshold = (BLACK + WHITE) / 2 
            
        DRIVE_SPEED = 100 
        PROPORTIONAL_GAIN = 1.2 
            
        while True: 
            deviation = line_sensor.reflection() - threshold
            turn_rate = PROPORTIONAL_GAIN * deviation 
            robot.drive(DRIVE_SPEED, turn_rate)
            wait(10)

     def sing(self, number_of_songs_played):
        print('SKILLS - Listen to the for', number_of_songs_played,'times')
        y = 1
        while y <= number_of_songs_played:
            ev3.speaker.beep(frequency=329.63, duration=500)
            ev3.speaker.beep(frequency=440, duration=500)
            ev3.speaker.beep(frequency=659.25, duration=500)
            ev3.speaker.beep(frequency=392, duration=500)
            ev3.speaker.beep(frequency=659.25, duration=500)
            ev3.speaker.beep(frequency=440, duration=500)
            ev3.speaker.beep(frequency=369.99, duration=500)
            ev3.speaker.beep(frequency=440, duration=500)
            ev3.speaker.beep(frequency=659.25, duration=500)
            ev3.speaker.beep(frequency=349.23, duration=500)
            ev3.speaker.beep(frequency=587.33, duration=250)
            ev3.speaker.beep(frequency=554.37, duration=250)
            ev3.speaker.beep(frequency=440, duration=500)
            i += 1

            ev3.speaker.beep(frequency=329.63, duration=500)
            ev3.speaker.beep(frequency=440, duration=500)
            ev3.speaker.beep(frequency=659.25, duration=500)
            ev3.speaker.beep(frequency=392, duration=500)
            ev3.speaker.beep(frequency=659.25, duration=500)
            ev3.speaker.beep(frequency=440, duration=500)
            ev3.speaker.beep(frequency=369.99, duration=500)
            ev3.speaker.beep(frequency=440, duration=500)
            ev3.speaker.beep(frequency=659.25, duration=500)
            ev3.speaker.beep(frequency=349.23, duration=500)
            ev3.speaker.beep(frequency=261.63, duration=500)
            ev3.speaker.beep(frequency=349.23, duration=500)
            ev3.speaker.beep(frequency=261.63, duration=750)
