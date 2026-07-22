# Results

## Objective

The objective of this experiment was to observe how changing the proportional gain (Kp) affects the performance of a simple closed-loop controller.

The controller was tested using four different Kp values while keeping all other parameters constant.

## Experimental Results

| Kp | Time to Reach Target (s) | Final True Angle (°) | Final Measured Angle (°) |
|----|-------------------------:|---------------------:|-------------------------:|
| 0.1 | 36.8 | 48.997 | 49.026 |
| 0.5 | 7.5 | 48.988 | 49.234 |
| 1.0 | 4.5 | 48.870 | 48.654 |
| 2.0 | 3.6 | 48.955 | 49.018 |

## Observations

- Increasing Kp reduced the time required to reach the target angle.
- A low Kp produced smooth but slow movement.
- Higher Kp values responded much faster while remaining stable in this simulation.
- Small differences between the true and measured angles were caused by the simulated sensor noise.

## Conclusion

This project demonstrated how proportional gain influences the behavior of a closed-loop controller.

Testing multiple Kp values showed the trade-off between response speed and controller aggressiveness. These concepts form the foundation of more advanced control systems used in robotic and biomedical applications.

## Next Steps

- Implement a PID controller.
- Connect the controller to an Arduino.
- Read real sensor data from an MPU6050.
- Compare simulated and experimental results.
