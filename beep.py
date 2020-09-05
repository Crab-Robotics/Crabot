#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick

ev3 = EV3Brick()
i = 1
while i < 3:
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

