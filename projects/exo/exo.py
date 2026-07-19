import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

starting_angle = 10
current_angle = starting_angle

target_angle = 50
time_step = 0.1
Kp = 0.5

errors = []
commands = []

max_command = 12
time = 0

times = []
angles = []
targets = []

while not (target_angle - 1 <= current_angle <= target_angle + 1):
    # Calculate how far the joint is from the target
    error = target_angle - current_angle

    # Proportional controller
    command = Kp * error

    # Limit the simulated actuator speed
    if command > max_command:
        command = max_command
    elif command < -max_command:
        command = -max_command

    # Update the simulated joint angle
    current_angle = current_angle + command * time_step

    # Update simulated time
    time = time + time_step

    times.append(time)
    angles.append(current_angle)
    targets.append(target_angle)

    errors.append(error)
    commands.append(command)
    
    print(
        f"Time: {time:.1f}s | "
        f"Angle: {current_angle:.2f}° | "
        f"Error: {error:.2f}° | "
        f"Command: {command:.2f}°/s"
    )


simulation_data = pd.DataFrame({
    "Time_s": times,
    "Target_Angle_deg": targets,
    "Current_Angle_deg": angles,
    "Error_deg": errors,
    "Command_deg_per_s": commands
})

data_folder = Path("data")
data_folder.mkdir(exist_ok=True)

simulation_data.to_csv(
    data_folder / "control_simulation.csv",
    index=False
)

print(simulation_data.head())

print("\nTarget reached.")
print(f"Final angle: {current_angle:.2f}°")
print(f"Total time: {time:.1f}s")

plt.plot(times, angles, label="Current Angle")
plt.plot(times, targets, label="Target Angle", linestyle="--")
plt.xlabel("Time (s)")
plt.ylabel("Angle (°)")
plt.title("Joint Angle Control Simulation")
plt.legend()
plt.grid()
plt.show()

plt.plot(times, errors)
plt.xlabel("Time (s)")
plt.ylabel("Error (degrees)")
plt.title("Joint Angle Error")
plt.grid()
plt.show()

plt.plot(times, commands)
plt.xlabel("Time (s)")
plt.ylabel("Command (degrees/second)")
plt.title("Controller Command")
plt.grid()
plt.show()