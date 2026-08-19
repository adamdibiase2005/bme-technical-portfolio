# Experiment Results

## Goal

Build a basic temperature data acquisition pipeline that reads a sensor signal with an Arduino, sends the data over Serial, saves it in Python, and analyzes the recorded temperature over time.
## Data

The Arduino sampled the temperature signal once per second and sent the readings to Python through Serial.

## Results
The synthetic warming trial had a baseline temperature of about 21.96 °C.

The temperature increased to a maximum of 22.8 °C at 22 seconds, then returned to about 21.99 °C by the end of the trial.

The Python script successfully loaded the CSV data and plotted temperature versus time.
