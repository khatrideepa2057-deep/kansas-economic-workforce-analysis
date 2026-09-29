import pandas as pd

# File paths
census_file = "data/raw/census_2024_kansas_counties.csv"
bls_file = "data/processed/bls_2024_kansas_counties.csv"

# Load the Census data
census_df = pd.read_csv(census_file)

# Load the BLS data
bls_df = pd.read_csv(bls_file)

# Check the size of each dataset
print("Census shape:", census_df.shape)
print("BLS shape:", bls_df.shape)

# Check the FIPS codes in both datasets
print("\nCensus FIPS:")
print(census_df[["county_name", "state_fips", "county_fips"]].head())

print("\nBLS FIPS:")
print(bls_df[["county_name", "state_fips", "county_fips"]].head())


# Make the FIPS codes the same type in both datasets
census_df["state_fips"] = census_df["state_fips"].astype(int)
census_df["county_fips"] = census_df["county_fips"].astype(int)

bls_df["state_fips"] = bls_df["state_fips"].astype(int)
bls_df["county_fips"] = bls_df["county_fips"].astype(int)

# Merge Census and BLS data using state and county FIPS codes
merged_df = census_df.merge(
    bls_df,
    on=["state_fips", "county_fips"],
    how="inner",
    suffixes=("_census", "_bls")
)

# Check the merged dataset
print("\nMerged shape:", merged_df.shape)

# Save the merged Census and BLS dataset
output_file = "data/processed/kansas_economic_workforce_2024.csv"

merged_df.to_csv(output_file, index=False)

print("Saved:", output_file)

