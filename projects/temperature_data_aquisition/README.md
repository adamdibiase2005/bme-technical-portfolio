# Temperature Data Acquisition System

## Overview

This project builds a simple temperature data acquisition system using an Arduino and Python.

The Arduino reads an analog temperature sensor signal, converts it to a temperature value, and sends the data to a computer through Serial communication. Python receives the data, saves it to CSV, and analyzes the temperature over time.

## Project Progression

### 1. Digital Output Test
LED blink test to verify the Arduino setup and understand digital outputs.

### 2. Analog Input Test
Potentiometer test to understand analog voltage measurement and the Arduino ADC range from 0 to 1023.

### 3. Temperature Sensor
LM35 used to convert an analog voltage into a temperature measurement.

### 4. Serial Data Logging
Arduino sent time, ADC, voltage, and temperature data to Python.

### 5. Python Analysis
Python saved the measurements to CSV and used pandas and matplotlib for analysis.

## Hardware

- Elegoo UNO R3
- LM35 temperature sensor
- Breadboard
- Jumper wires
- USB cable

## Software

- Arduino IDE
- Python
- pyserial
- pandas
- matplotlib

## How It Works

1. The LM35 produces an analog voltage related to temperature.
2. The Arduino reads this voltage using its analog-to-digital converter.
3. The ADC reading is converted to voltage and then temperature.
4. The Arduino sends the data through Serial at one sample per second.
5. Python reads the Serial data and saves it to a CSV file.
6. pandas and matplotlib are used to analyze and plot the data.

The data format used was:
time_ms,adc,voltage,temperature_C

## Results

- Baseline temperature: approximately 21.96 °C
- Maximum temperature: 22.8 °C
- Time of maximum temperature: 22 seconds
- Final temperature: approximately 21.99 °C
