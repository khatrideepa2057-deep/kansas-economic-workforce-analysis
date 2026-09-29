import requests
import pandas as pd
import os
from dotenv import load_dotenv

# Load the Census API key from the .env file
load_dotenv()
api_key = os.getenv("CENSUS_API_KEY")

# Choose the Census dataset
year = "2024"
dataset = "acs/acs5"

# Select the Census variables we want
variables = [
    "NAME",
    "B01003_001E",
    "B19013_001E",
    "B23025_002E",
    "B23025_001E",
    "B23025_005E",
    "B17001_001E",
    "B17001_002E",
    "B15003_001E",
    "B15003_022E",
    "B15003_023E",
    "B15003_024E",
    "B15003_025E"
]



# Build the Census API URL
base_url = f"https://api.census.gov/data/{year}/{dataset}"

# Set the API request parameters
params = {
    "get": ",".join(variables),
    "for": "county:*",
    "in": "state:20",
    "key": api_key
}

# Send the request to the Census API
response = requests.get(base_url, params=params)

# Check whether the request worked
print("Status code:", response.status_code)

# Convert the Census response into Python data
data = response.json()

# Convert the data into a Pandas DataFrame
df = pd.DataFrame(data[1:], columns=data[0])

# Rename the columns
df = df.rename(columns={
    "NAME": "county_name",
    "B01003_001E": "population",
    "B19013_001E": "median_household_income",
    "B23025_002E": "civilian_labor_force",
    "B23025_001E": "population_16_plus",
    "B23025_005E": "unemployed",
    "B17001_001E": "poverty_universe",
    "B17001_002E": "below_poverty",
    "B15003_001E": "population_25_plus",
    "B15003_022E": "bachelors_degree",
    "B15003_023E": "masters_degree",
    "B15003_024E": "professional_degree",
    "B15003_025E": "doctorate_degree",
    "state": "state_fips",
    "county": "county_fips"
})



# Convert the labor force and poverty columns to numbers
df["civilian_labor_force"] = pd.to_numeric(df["civilian_labor_force"])
df["population_16_plus"] = pd.to_numeric(df["population_16_plus"])
df["unemployed"] = pd.to_numeric(df["unemployed"])
df["poverty_universe"] = pd.to_numeric(df["poverty_universe"])
df["below_poverty"] = pd.to_numeric(df["below_poverty"])


# Convert the education columns to numbers
df["population_25_plus"] = pd.to_numeric(df["population_25_plus"])
df["bachelors_degree"] = pd.to_numeric(df["bachelors_degree"])
df["masters_degree"] = pd.to_numeric(df["masters_degree"])
df["professional_degree"] = pd.to_numeric(df["professional_degree"])
df["doctorate_degree"] = pd.to_numeric(df["doctorate_degree"]) 



# Calculate the labor force participation rate
df["labor_force_participation_rate"] = (
    df["civilian_labor_force"] / df["population_16_plus"] * 100
).round(2)

# Calculate the unemployment rate
df["unemployment_rate"] = (
    df["unemployed"] / df["civilian_labor_force"] * 100
).round(2)

# Calculate the poverty rate
df["poverty_rate"] = (
    df["below_poverty"] / df["poverty_universe"] * 100
).round(2)

# Calculate the number of adults age 25+ with a bachelor's degree or higher
df["bachelors_or_higher"] = (
    df["bachelors_degree"]
    + df["masters_degree"]
    + df["professional_degree"]
    + df["doctorate_degree"]
)

# Calculate bachelor's degree or higher rate
df["bachelors_or_higher_rate"] = (
    df["bachelors_or_higher"] / df["population_25_plus"] * 100
).round(2)



# Display the first 5 rows
print(df.head())


# Save the data
output_file = "data/raw/census_2024_kansas_counties.csv"
df.to_csv(output_file, index=False)

print("Saved:", output_file)
print("Total counties:", len(df))
