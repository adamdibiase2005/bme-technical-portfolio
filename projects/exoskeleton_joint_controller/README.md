# Exoskeleton Joint Controller Simulation

This project simulates a simple knee joint controller for an exoskeleton using Python. The goal was to understand the basics of closed-loop control before applying the same concepts to real hardware with Arduino and sensors.

## Project Overview

The simulation moves a virtual knee joint from an initial angle to a target angle using a proportional (P) controller. At each time step, the controller measures the joint angle, calculates the error, and sends a command to reduce that error.

To make the simulation more realistic, Gaussian sensor noise is added to the measured angle, and the controller output is limited to simulate the maximum speed of a real actuator.

## Features

- Proportional (P) controller
- Adjustable controller gain (Kp)
- Sensor noise simulation
- Actuator speed limit
- CSV data logging
- Angle vs. time visualization
- Controller tuning by testing multiple Kp values

## Files

```
projects/
└── exoskeleton_joint_controller/
    ├── exo_joint.py
    ├── README.md
    └── data/
        ├── control_simulation_Kp_0.1.csv
        ├── control_simulation_Kp_0.5.csv
        ├── control_simulation_Kp_1.csv
        └── control_simulation_Kp_2.csv
```

## What I Learned

Through this project I learned how:

- feedback control works
- a proportional controller calculates its output
- controller gain (Kp) affects response speed
- sensor noise influences measurements
- CSV files can be generated automatically using pandas
- Python can be used to simulate engineering systems before building hardware

