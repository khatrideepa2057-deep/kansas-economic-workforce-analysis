import pandas as pd
import sqlite3

# Load the final merged Kansas dataset
file_path = "data/processed/kansas_economic_workforce_2024.csv"
df = pd.read_csv(file_path)

# Select the columns needed for SQL analysis
sql_df = df[
    [
        "state_fips",
        "county_fips",
        "county_name_census",
        "population",
        "median_household_income",
        "labor_force_participation_rate",
        "unemployment_rate_bls",
        "poverty_rate",
        "bachelors_or_higher_rate",
        "labor_force",
        "employed",
        "unemployed_bls"
    ]
].copy()

# Rename columns for the SQL table
sql_df = sql_df.rename(columns={
    "county_name_census": "county_name",
    "unemployment_rate_bls": "unemployment_rate",
    "unemployed_bls": "unemployed"
})

# Connect to a SQLite database
connection = sqlite3.connect(
    "data/processed/kansas_economic_workforce.db"
)

# Load the data into the SQL table
sql_df.to_sql(
    "kansas_county_economic_data",
    connection,
    if_exists="replace",
    index=False
)

# Check how many rows were loaded
row_count = pd.read_sql_query(
    "SELECT COUNT(*) AS total_rows FROM kansas_county_economic_data",
    connection
)

print(row_count)

# Close the database connection
connection.close()

print("Database created successfully.")

