from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


# show all columns when printing
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)


# main project folders
project_folder = Path(__file__).resolve().parent.parent
data_folder = project_folder / "data"
outputs_folder = project_folder / "outputs"
charts_folder = outputs_folder / "charts"

# make the output folders if they do not exist
outputs_folder.mkdir(exist_ok=True)
charts_folder.mkdir(exist_ok=True)


# columns every input file needs
required_columns = [
    "Year",
    "Revenue",
    "Gross Profit",
    "Operating Income",
    "Net Income",
    "Operating Cash Flow",
    "Capital Expenditures",
    "Free Cash Flow",
]


# kpis that will be calculated
kpi_columns = [
    "Revenue Growth (%)",
    "Gross Margin (%)",
    "Operating Margin (%)",
    "Net Margin (%)",
    "Operating Cash Flow Margin (%)",
    "Capex as % of Revenue",
    "Free Cash Flow Margin (%)",
]


# load one csv file
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data


# check if the data can be analyzed
def validate_data(data, required_columns):
    missing_columns = []

    for column in required_columns:
        if column not in data.columns:
            missing_columns.append(column)

    if missing_columns:
        print("Missing required columns:", missing_columns)
        return False

    non_numeric_columns = []

    for column in required_columns:
        if not pd.api.types.is_numeric_dtype(data[column]):
            non_numeric_columns.append(column)

    if non_numeric_columns:
        print("Columns that are not numeric:", non_numeric_columns)
        return False

    print("All required columns are present.")
    print("All required columns are numeric.")

    columns_with_missing_values = []

    for column in required_columns:
        if data[column].isna().sum() > 0:
            columns_with_missing_values.append(column)

    if columns_with_missing_values:
        print("Columns with missing values:", columns_with_missing_values)
    else:
        print("No missing values in required columns.")

    return True


# calculate all financial kpis
def calculate_kpis(data):
    previous_revenue = data["Revenue"].shift(1)

    data["Revenue Growth (%)"] = (
        (data["Revenue"] - previous_revenue)
        / previous_revenue
    ) * 100

    data["Gross Margin (%)"] = (
        data["Gross Profit"] / data["Revenue"]
    ) * 100

    data["Operating Margin (%)"] = (
        data["Operating Income"] / data["Revenue"]
    ) * 100

    data["Net Margin (%)"] = (
        data["Net Income"] / data["Revenue"]
    ) * 100

    data["Operating Cash Flow Margin (%)"] = (
        data["Operating Cash Flow"] / data["Revenue"]
    ) * 100

    data["Capex as % of Revenue"] = (
        data["Capital Expenditures"] / data["Revenue"]
    ) * 100

    data["Free Cash Flow Margin (%)"] = (
        data["Free Cash Flow"] / data["Revenue"]
    ) * 100

    data[kpi_columns] = data[kpi_columns].round(2)

    return data


# make and save the clean summary
def export_summary(data, company_name):
    summary_columns = ["Year"] + kpi_columns
    kpi_summary = data[summary_columns]

    output_path = (
        outputs_folder
        / f"{company_name}_kpi_summary.csv"
    )

    kpi_summary.to_csv(output_path, index=False)

    print("\nKPI summary:")
    print(kpi_summary)

    print("\nSaved summary to:")
    print(output_path)


# make the three charts
def create_charts(data, company_name):
    revenue_chart_path = (
        charts_folder
        / f"{company_name}_revenue_by_year.png"
    )

    plt.figure()
    plt.plot(
        data["Year"],
        data["Revenue"],
        marker="o",
    )
    plt.title(f"{company_name} Revenue by Year")
    plt.xlabel("Year")
    plt.ylabel("Revenue (USD millions)")
    plt.xticks(data["Year"])
    plt.savefig(revenue_chart_path)
    plt.close()

    net_income_chart_path = (
        charts_folder
        / f"{company_name}_net_income_by_year.png"
    )

    plt.figure()
    plt.plot(
        data["Year"],
        data["Net Income"],
        marker="o",
    )
    plt.title(f"{company_name} Net Income by Year")
    plt.xlabel("Year")
    plt.ylabel("Net Income (USD millions)")
    plt.xticks(data["Year"])
    plt.savefig(net_income_chart_path)
    plt.close()

    profitability_chart_path = (
        charts_folder
        / f"{company_name}_profitability_margins.png"
    )

    plt.figure()

    plt.plot(
        data["Year"],
        data["Gross Margin (%)"],
        marker="o",
        label="Gross Margin",
    )

    plt.plot(
        data["Year"],
        data["Operating Margin (%)"],
        marker="o",
        label="Operating Margin",
    )

    plt.plot(
        data["Year"],
        data["Net Margin (%)"],
        marker="o",
        label="Net Margin",
    )

    plt.title(f"{company_name} Profitability Margins by Year")
    plt.xlabel("Year")
    plt.ylabel("Margin (%)")
    plt.xticks(data["Year"])
    plt.legend()
    plt.savefig(profitability_chart_path)
    plt.close()

    print("\nCharts saved:")
    print(revenue_chart_path)
    print(net_income_chart_path)
    print(profitability_chart_path)


# run the full analyzer for one company
def analyze_company(file_name, company_name):
    print("\n--------------------------------")
    print("Analyzing:", company_name)
    print("--------------------------------")

    csv_path = data_folder / file_name

    financial_data = load_data(csv_path)

    data_is_valid = validate_data(
        financial_data,
        required_columns,
    )

    if not data_is_valid:
        print("Analysis stopped for:", company_name)
        return

    # make sure the years are in the correct order
    financial_data = financial_data.sort_values(
        "Year"
    ).reset_index(drop=True)

    financial_data = calculate_kpis(financial_data)

    print("\nFull financial data with KPIs:")
    print(financial_data)

    export_summary(financial_data, company_name)
    create_charts(financial_data, company_name)


# analyze both csv files
analyze_company(
    "intuitive_surgical.csv",
    "intuitive_surgical",
)

analyze_company(
    "stryker.csv",
    "stryker",
)