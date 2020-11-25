#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import CrabRobotLibrary


# Define Class Robot
class Richard_Skills:

    def __init__(self, robot):
        self.robot = robot
        self.color_sensor_left = ColorSensor(Port.S3)
        self.color_sensor_right = ColorSensor(Port.S4)

    def tell_me_about_your_skills(self):
        print("SKILLS - I can Dance, Wiggle, Big Wiggle, and Shuffle")
        print("SKILLS - I have access to information like wheel diameter, see",self.robot.wheel_diameter)
        print()

    def dance(self, number_of_dances):
        print("SKILLS - Perform", number_of_dances,"dance moves.")
        y = 1
        while y <= number_of_dances:
            self.robot.turn(360)
            y = y + 1

    def wiggle(self, number_of_wiggles):
        print("SKILLS - Wiggle",number_of_wiggles,"times.")
        z = 1
        while z <= number_of_wiggles:
            self.robot.turn(45)
            self.robot.turn(-45)
            z = z + 1

    def shuffle(self, number_of_shuffles):
        print("SKILLS - Shuffle",number_of_shuffles,"times.")
        a = 1
        while a <= number_of_shuffles:
            self.robot.move_forward(50)
            self.robot.move_backwards(50)
            a = a + 1

    def big_wiggle(self, number_of_big_wiggles):
        print("SKILLS - Big Wiggle", number_of_big_wiggles, "times")
        b = 1
        while b <= number_of_big_wiggles:
            self.robot.turn(45)
            self.robot.turn(-15)
            b = b + 1
    
    def detect_color(self):
        print("I can see left",self.color_sensor_left.color()," and right", self.color_sensor_right.color(),".")

    def detect_wall(self, distance_mm, angle_turn):
        ultrasonic_sensor = UltrasonicSensor(Port.S1)
        print("If I get too close to the wall, I will turn.")
        if self.ultrasonic_sensor.distance() <= distance_mm:
            print("Too close!")
            self.robot.turn(angle_turn) 
        else:
            print("There is some room...")
    
    def under_bar_and_dance():
        Crabot.move_forward(950)
        Crabot.turn(90)
        Crabot.move_forward(400)
        Crabot.turn(45)
        Crabot.move_forward(390)

    def speed_and_power(distance):
        Crabot.gyro_drive(200000000000000000, 0, distance)