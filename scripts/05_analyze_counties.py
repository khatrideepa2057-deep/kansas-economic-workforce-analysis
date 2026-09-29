import pandas as pd

# Load the final merged dataset
file_path = "data/processed/kansas_economic_workforce_2024.csv"
df = pd.read_csv(file_path)

# Select the main indicators we will use in the analysis
analysis_df = df[
    [
        "county_name_census",
        "population",
        "median_household_income",
        "labor_force_participation_rate",
        "unemployment_rate_bls",
        "poverty_rate",
        "bachelors_or_higher_rate"
    ]
].copy()

# Rename county name to make it easier to use
analysis_df = analysis_df.rename(
    columns={"county_name_census": "county_name"}
)

# Find the 10 counties with the highest unemployment rates
highest_unemployment = analysis_df.sort_values(
    by="unemployment_rate_bls",
    ascending=False
).head(10)

# Find the 10 counties with the lowest unemployment rates
lowest_unemployment = analysis_df.sort_values(
    by="unemployment_rate_bls",
    ascending=True
).head(10)

print("\n10 Kansas Counties with Highest Unemployment Rates:")
print(
    highest_unemployment[
        ["county_name", "unemployment_rate_bls"]
    ].to_string(index=False)
)

print("\n10 Kansas Counties with Lowest Unemployment Rates:")
print(
    lowest_unemployment[
        ["county_name", "unemployment_rate_bls"]
    ].to_string(index=False)
)

# Select indicators for correlation analysis
correlation_columns = [
    "unemployment_rate_bls",
    "poverty_rate",
    "median_household_income",
    "bachelors_or_higher_rate",
    "labor_force_participation_rate"
]

# Show all columns in the terminal
pd.set_option("display.max_columns", None)

# Calculate correlations between the economic indicators
correlation_matrix = analysis_df[correlation_columns].corr()

print("\nCorrelation Matrix:")
print(correlation_matrix.round(2))



