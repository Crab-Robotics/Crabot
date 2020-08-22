#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Define Class Robot

class Robot:
    brick = EV3Brick()
    left_wheel = Motor(Port.A)
    right_wheel = Motor(Port.D)
    wheel_diameter = 95
    axle_track = 120
    robot = DriveBase(left_wheel, right_wheel, wheel_diameter, axle_track)

    def __init__(self, name, mood):
        self.name = name
        self.mood = mood

    def tell_me_about_yourself(self):
        print("The robot's name is " + self.name + ".")
        print("This robot is " + self.mood + ".")
        print("Wheel diameter is", self.wheel_diameter, ".")
        print("Axle Track is", self.axle_track, ".")
        print()

    def move_forward(self, distance_mm):
        print("Move forward", distance_mm, ".")
        self.robot.straight(-distance_mm)
      
    def turn(self, angle):
        print("Turn", angle, "degrees.")
        self.robot.turn(angle)

    def beep(self, number_of_beeps):
        print("Beep",number_of_beeps,"times.")
        x = 1
        while x <= number_of_beeps: 
            self.brick.speaker.beep()
            wait(30)
            x = x + 1

    def move_backwards(self, distance_mm):
        print("Move backwards",distance_mm,".")
        self.robot.straight(distance_mm)