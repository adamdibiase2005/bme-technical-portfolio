import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path

# Make the simulated noise repeatable while debugging
np.random.seed(42)

starting_angle = 10
current_angle = starting_angle
target_angle = 50

time_step = 0.1
Kp = 0.1
max_command = 12
sensor_noise_std = 0.3

time = 0

times = []
targets = []
true_angles = []
measured_angles = []
errors = []
commands = []

while not (target_angle - 1 <= current_angle <= target_angle + 1):

    # Simulated sensor measurement
    measured_angle = current_angle + np.random.normal(
        loc=0,
        scale=sensor_noise_std
    )

    # The controller only uses the measured angle
    error = target_angle - measured_angle

    # Proportional controller
    command = Kp * error

    # Simulated actuator limit
    if command > max_command:
        command = max_command
    elif command < -max_command:
        command = -max_command

    # Store the system state at this time
    times.append(time)
    targets.append(target_angle)
    true_angles.append(current_angle)
    measured_angles.append(measured_angle)
    errors.append(error)
    commands.append(command)

    print(
        f"Time: {time:.1f}s | "
        f"True angle: {current_angle:.2f}° | "
        f"Measured angle: {measured_angle:.2f}° | "
        f"Error: {error:.2f}° | "
        f"Command: {command:.2f}°/s"
    )

    # Simulate the physical joint responding
    current_angle = current_angle + command * time_step

    # Move to the next sample
    time = time + time_step


simulation_data = pd.DataFrame({
    "Time_s": times,
    "Target_Angle_deg": targets,
    "True_Angle_deg": true_angles,
    "Measured_Angle_deg": measured_angles,
    "Error_deg": errors,
    "Command_deg_per_s": commands
})


data_folder = Path("data")
data_folder.mkdir(exist_ok=True)

csv_path = data_folder / f"control_simulation_Kp_{Kp}.csv"

simulation_data.to_csv(
    csv_path,
    index=False
)


print("\nTarget reached.")
print(f"Final true angle: {current_angle:.2f}°")
print(f"Total time: {time:.1f}s")
print(f"Maximum command: {max(abs(value) for value in commands):.2f}°/s")
print(f"CSV saved to: {csv_path}")
print("\nFirst five rows:")
print(simulation_data.head())


# Graph 1: target, true angle and measured angle
plt.figure()

plt.plot(
    times,
    true_angles,
    label="True Angle"
)

plt.plot(
    times,
    measured_angles,
    label="Measured Angle",
    alpha=0.6
)

plt.plot(
    times,
    targets,
    label="Target Angle",
    linestyle="--"
)

plt.xlabel("Time (s)")
plt.ylabel("Angle (degrees)")
plt.title("Exoskeleton Joint Control with Sensor Noise")
plt.legend()
plt.grid()
plt.show()


# Graph 2: controller error
plt.figure()

plt.plot(times, errors)

plt.xlabel("Time (s)")
plt.ylabel("Error (degrees)")
plt.title("Joint Angle Error")
plt.grid()
plt.show()


# Graph 3: controller command
plt.figure()

plt.plot(times, commands)

plt.xlabel("Time (s)")
plt.ylabel("Command (degrees/second)")
plt.title("Controller Command")
plt.grid()
plt.show()

print(f"Maximum command: {max(abs(value) for value in commands):.2f}°/s")