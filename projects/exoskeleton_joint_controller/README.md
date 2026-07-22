# Exoskeleton Joint Controller Simulation

## Overview

This project is my first step toward understanding how lower-limb exoskeletons use feedback control to move a joint to a desired position.

Using Python, I built a simulation of a single knee joint controlled by a proportional (P) controller. The program measures the joint angle, calculates the error between the current and desired position, and generates a control command that moves the joint toward the target angle.

The simulation also includes actuator limits and simulated sensor noise to better represent how a real system behaves.

## Objectives

- Learn the fundamentals of closed-loop control
- Simulate joint motion using Python
- Understand the effect of proportional gain (Kp)
- Introduce realistic sensor noise
- Export experimental data for analysis

## How It Works

The controller repeats the following steps until the joint reaches the target angle:

1. Read the measured joint angle.
2. Calculate the position error.
3. Compute the control command using a proportional controller.
4. Limit the command to the actuator's maximum speed.
5. Update the joint position.
6. Save the data for later analysis.

## Features

- Closed-loop proportional controller
- Adjustable proportional gain (Kp)
- Simulated Gaussian sensor noise
- Actuator saturation
- CSV data logging
- Multiple controller tuning experiments

## Results

The controller was tested using several proportional gains:

- Kp = 0.1
- Kp = 0.5
- Kp = 1.0
- Kp = 2.0

Comparing these simulations showed how increasing Kp reduces the time required to reach the target while changing the controller's behavior.

## Skills Practiced

- Python
- NumPy
- Pandas
- Matplotlib
- Control systems fundamentals
- Engineering simulation
- Data analysis
