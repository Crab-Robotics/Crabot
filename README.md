# C.R.A.B. Robotics Team #39374

We are a [FIRST Lego League](https://www.firstlegoleague.org/) team, and this is where we post edits and new code onto our robot. 

## Introduction

We wrote our programs in [Python](https://www.python.org/) this season. Python is a text-based programming language that’s used in the real world. It’s more powerful than the block programming language; allowing us to have more control over our motors and sensors and use a library of functions.

One example of how Python is more powerful is our [`gyro_drive_until_white()`](https://github.com/Crab-Robotics/Crabot/blob/master/CrabRobotLibrary.py#L172-L182) function. This is a function we wrote that uses two sensors values inside of a loop, which would be difficult or impossible with block programming. We had to write the function from scratch because there wasn’t anyone who’d already written something like this.

Using Python also means that we can put our code on Github. This lets us work on it together, and merge changes using [pull requests](https://github.com/Crab-Robotics/Crabot/pulls). This was very important because most of our team was virtual this season. We enrolled in [Hacktoberfest](https://hacktoberfest.digitalocean.com/), and each our of team members submitted [4 pull requests in order to get a free t-shirt](https://github.com/Crab-Robotics/Crabot/pull/6).

## Summary

Our main program is called [`uber.py`](https://github.com/Crab-Robotics/Crabot/blob/master/uber.py), and we use it to run all of the missions we complete as part of the challenge. The program starts an infinite loop (that means it runs forever) and waits for a button press. Then, depending on which button is pressed, it runs a different program. The programs it runs are:

- **UP**: [`run_basketball.py`](https://github.com/Crab-Robotics/Crabot/blob/master/run_basketball.py)
- **RIGHT**: [`run_cube.py`](https://github.com/Crab-Robotics/Crabot/blob/master/run_cube.py)
- **DOWN**: [`run_treadmill.py`](https://github.com/Crab-Robotics/Crabot/blob/master/run_treadmill.py)
- **LEFT**: [`run_cheese.py`](https://github.com/Crab-Robotics/Crabot/blob/master/run_cheese.py)

## Libraries
We currently have these libraies in our repository.

[CrabRobotLibrary](https://github.com/Crab-Robotics/Crabot/blob/master/CrabRobotLibrary.py):
 - `tell_me_about_your_skills()` 
 - `coast()`
 - `move_forward()`
 - `move_backwards()`
 - `turn()`
 - `front_activate(speed, rotation_angle, direction)`
 - `front_reset(direction)`
 - `front_forever(speed, direction)`
 - `back_activate(speed, rotation_angle, direction)`
 - `back_reset(direction)`
 - `back_forever(speed, direction)`
 - `back_brake()`
 - `reset_attachments()`
 - `reset_elevator()`
 - `gyro_reset()`
 - `gyro_turn()`
 - `gyro_drive()`
 - `gyro_drive_until_white()`
 - `bw_gyro_drive()`
 - `beep()`

[RichardSkillsLibrary](https://github.com/Crab-Robotics/Crabot/blob/master/RichardSkillsLibrary.py):
 - `tell_me_about_your_skills()`
 - `dance()`
 - `wiggle()`
 - `shuffle()`
 - `big_wiggle()`
 - `detect_color()`

[Caleb_Skills_Library](https://github.com/Crab-Robotics/Crabot/blob/master/Caleb_Skills_Library.py):
 - `tell_me_about_your_skills()`

[GreydenSkillsLibrary](https://github.com/Crab-Robotics/Crabot/blob/master/GreydenSkillsLibrary.py):
 - `tell_me_about_your_skills()`

[KateSkillsLibrary](https://github.com/Crab-Robotics/Crabot/blob/master/KateSkillsLibrary.py):
 - `tell_me_about_your_skills()`

[ZacSkillsLibrary](https://github.com/Crab-Robotics/Crabot/blob/master/ZacSkillsLibrary.py):
 - `tell_me_about_your_skills()`
 - `run()`
 - `follow()`

SNAP! SNAP!
