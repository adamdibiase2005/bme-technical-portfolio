import serial
import time
import csv

ser = serial.Serial("COM3", 9600, timeout=2)

time.sleep(2)

ser.readline()  # discard first line

with open("baseline_trial.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["time_ms", "adc", "voltage", "temperature_C"])

    for i in range(60):
        line = ser.readline().decode().strip()

        parts = line.split(",")

        time_ms = int(parts[0])
        adc = int(parts[1])
        voltage = float(parts[2])
        temperature = float(parts[3])

        writer.writerow([time_ms, adc, voltage, temperature])

        print(time_ms, adc, voltage, temperature)

ser.close()