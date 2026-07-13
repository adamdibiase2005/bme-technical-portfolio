# Financial KPI Analyzer

## Overview

This is a Python project that reads company financial data from CSV files and calculates a set of basic financial KPIs.

I originally did this type of analysis manually in Excel, so the goal here was to automate part of that process and make it work for more than one company.

## What it does

The program:

- loads financial data from a CSV
- checks that the required columns are there
- checks that the data is numeric
- shows where values are missing
- calculates financial KPIs
- exports a clean summary CSV
- creates three charts for each company

I tested it using Intuitive Surgical and Stryker.

## Technologies

- Python
- pandas
- matplotlib
- pathlib

## Project structure

```text
python_financial_kpi_analyzer/
├── README.md
├── data/
│   ├── intuitive_surgical.csv
│   └── stryker.csv
├── src/
│   └── analyzer.py
└── outputs/
    ├── surgical_kpi_summary.csv
    ├── stryker_kpi_summary.csv
    └── charts/
