import pandas as pd

# Path to the BLS county annual averages file
file_path = "data/raw/laucnty24.xlsx"

# Read the BLS Excel file
df = pd.read_excel(file_path, header=1)

# Filter the data to Kansas counties only
kansas_df = df[df["State FIPS Code"] == 20].copy()

# Keep only the columns needed for the analysis
kansas_df = kansas_df[
    [
        "State FIPS Code",
        "County FIPS Code",
        "County Name/State Abbreviation",
        "Year",
        "Labor Force",
        "Employed",
        "Unemployed",
        "Unemployment Rate (%)"
    ]
]

# Rename the columns
kansas_df = kansas_df.rename(columns={
    "State FIPS Code": "state_fips",
    "County FIPS Code": "county_fips",
    "County Name/State Abbreviation": "county_name",
    "Year": "year",
    "Labor Force": "labor_force",
    "Employed": "employed",
    "Unemployed": "unemployed",
    "Unemployment Rate (%)": "unemployment_rate"
})

# Display the first 5 rows
print(kansas_df.head())

# Display the cleaned column names
print(kansas_df.columns.tolist())

# Display the total number of Kansas counties
print("Total Kansas counties:", len(kansas_df))

# Save the cleaned Kansas BLS data
output_file = "data/processed/bls_2024_kansas_counties.csv"

kansas_df.to_csv(output_file, index=False)

print("Saved:", output_file)

