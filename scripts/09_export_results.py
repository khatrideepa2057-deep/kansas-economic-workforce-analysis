import pandas as pd
import os

# Load the final merged Kansas county dataset
file_path = "data/processed/kansas_economic_workforce_2024.csv"
df = pd.read_csv(file_path)

# Create a folder for analysis result tables
output_folder = "outputs/tables"
os.makedirs(output_folder, exist_ok=True)

# Check that the dataset loaded correctly
print("Dataset shape:", df.shape)

print("Results folder ready:", output_folder)

# Create the Top 10 counties by unemployment rate table
top_10_unemployment = df[
    [
        "county_name_census",
        "unemployment_rate_bls",
        "poverty_rate",
        "labor_force_participation_rate"
    ]
].sort_values(
    by="unemployment_rate_bls",
    ascending=False
).head(10)

# Rename columns for cleaner output
top_10_unemployment = top_10_unemployment.rename(columns={
    "county_name_census": "county_name",
    "unemployment_rate_bls": "unemployment_rate"
})

# Save the table
top_10_unemployment.to_csv(
    "outputs/tables/top_10_unemployment.csv",
    index=False
)

print("Saved: outputs/tables/top_10_unemployment.csv")

# Select variables for the correlation table
correlation_columns = [
    "unemployment_rate_bls",
    "poverty_rate",
    "median_household_income",
    "bachelors_or_higher_rate",
    "labor_force_participation_rate"
]

# Calculate the correlation matrix
correlation_matrix = df[correlation_columns].corr().round(2)

# Save the correlation matrix
correlation_matrix.to_csv(
    "outputs/tables/correlation_matrix.csv"
)

print("Saved: outputs/tables/correlation_matrix.csv")

# Create the 10 counties with the lowest labor-force participation rates
lowest_labor_force = df[
    [
        "county_name_census",
        "labor_force_participation_rate",
        "unemployment_rate_bls",
        "poverty_rate"
    ]
].sort_values(
    by="labor_force_participation_rate",
    ascending=True
).head(10)

# Rename columns for cleaner output
lowest_labor_force = lowest_labor_force.rename(columns={
    "county_name_census": "county_name",
    "unemployment_rate_bls": "unemployment_rate"
})

# Save the table
lowest_labor_force.to_csv(
    "outputs/tables/lowest_labor_force_participation.csv",
    index=False
)

print("Saved: outputs/tables/lowest_labor_force_participation.csv")

# Create the 10 counties with the highest bachelor's-or-higher rates
top_education = df[
    [
        "county_name_census",
        "bachelors_or_higher_rate",
        "median_household_income"
    ]
].sort_values(
    by=["bachelors_or_higher_rate", "median_household_income"],
    ascending=[False, False]
).head(10)

# Rename county column
top_education = top_education.rename(columns={
    "county_name_census": "county_name"
})

# Save the table
top_education.to_csv(
    "outputs/tables/top_education_income.csv",
    index=False
)

print("Saved: outputs/tables/top_education_income.csv")

