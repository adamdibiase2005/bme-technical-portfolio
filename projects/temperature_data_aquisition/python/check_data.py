import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("baseline_trial.csv")

print("Baseline mean:", df["temperature_C"].iloc[:10].mean())
print("Maximum temperature:", df["temperature_C"].max())
print(
    "Time to maximum (ms):",
    df.loc[df["temperature_C"].idxmax(), "time_ms"]
)
print("Final temperature:", df["temperature_C"].iloc[-1])

plt.plot(df["time_ms"] / 1000, df["temperature_C"])

plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.title("Synthetic Temperature Response")
plt.grid()

plt.show()

