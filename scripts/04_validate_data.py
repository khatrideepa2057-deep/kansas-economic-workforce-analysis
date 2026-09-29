import pandas as pd

# Load the merged Census + BLS dataset
file_path = "data/processed/kansas_economic_workforce_2024.csv"

df = pd.read_csv(file_path)

# Check dataset size
print("Dataset shape:", df.shape)

# Check for duplicate counties
print("Duplicate counties:", df.duplicated(
    subset=["state_fips", "county_fips"]
).sum())

# Check missing values in each column
print("\nMissing values:")
print(df.isnull().sum())

# Check that all Kansas counties are present
print("\nTotal unique counties:", df["county_fips"].nunique())

# Display basic statistics for important indicators
print("\nSummary statistics:")
print(
    df[
        [
            "population",
            "median_household_income",
            "labor_force_participation_rate",
            "poverty_rate",
            "bachelors_or_higher_rate",
            "unemployment_rate_bls"
        ]
    ].describe()
)

