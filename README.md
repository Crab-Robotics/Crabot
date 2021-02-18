# C.R.A.B. Robotics Team #39374

We are a [FIRST Lego League](https://www.firstlegoleague.org/) team, and this is where we post edits and new code onto our robot. 

## Features

Our main program is called [`uber.py`](https://github.com/Crab-Robotics/Crabot/blob/master/uber.py), and we use it to run all of the missions we complete as part of the challenge. The program starts an infinite loop (that means it runs forever) that waits for a button press. Then, depending on which button is pressed, it runs a different program. The programs it runs are:

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
