import pandas as pd
import matplotlib.pyplot as plt

# Load the final merged dataset
file_path = "data/processed/kansas_economic_workforce_2024.csv"
df = pd.read_csv(file_path)

# Create a scatter plot:
# Poverty Rate vs. Median Household Income
plt.figure(figsize=(10, 6))

plt.scatter(
    df["median_household_income"],
    df["poverty_rate"]
)

# Add chart title and axis labels
plt.title("Poverty Rate vs. Median Household Income in Kansas Counties (2024)")
plt.xlabel("Median Household Income ($)")
plt.ylabel("Poverty Rate (%)")

# Make the layout cleaner
plt.tight_layout()

# Save the chart
output_file = "outputs/charts/poverty_vs_income.png"
plt.savefig(output_file, dpi=300)

# Display the chart
plt.show()

print("Saved:", output_file)

# Create a scatter plot:
# Unemployment Rate vs. Labor Force Participation Rate
plt.figure(figsize=(10, 6))

plt.scatter(
    df["labor_force_participation_rate"],
    df["unemployment_rate_bls"]
)

# Add chart title and axis labels
plt.title("Unemployment vs. Labor Force Participation in Kansas Counties (2024)")
plt.xlabel("Labor Force Participation Rate (%)")
plt.ylabel("Unemployment Rate (%)")

# Make the layout cleaner
plt.tight_layout()

# Save the chart
output_file = "outputs/charts/unemployment_vs_labor_force.png"
plt.savefig(output_file, dpi=300)

# Display the chart
plt.show()

print("Saved:", output_file)

# Create a scatter plot:
# Bachelor's Degree or Higher Rate vs. Median Household Income
plt.figure(figsize=(10, 6))

plt.scatter(
    df["bachelors_or_higher_rate"],
    df["median_household_income"]
)

# Add chart title and axis labels
plt.title("Education vs. Median Household Income in Kansas Counties (2024)")
plt.xlabel("Bachelor's Degree or Higher (%)")
plt.ylabel("Median Household Income ($)")

# Make the layout cleaner
plt.tight_layout()

# Save the chart
output_file = "outputs/charts/education_vs_income.png"
plt.savefig(output_file, dpi=300)

# Display the chart
plt.show()

print("Saved:", output_file)

# Find the 10 counties with the highest unemployment rates
top_10_unemployment = df.nlargest(
    10,
    "unemployment_rate_bls"
).copy()

# Use shorter county names for the chart
top_10_unemployment["county_label"] = (
    top_10_unemployment["county_name_census"]
    .str.replace(" County, Kansas", "", regex=False)
)

# Sort for a horizontal bar chart
top_10_unemployment = top_10_unemployment.sort_values(
    "unemployment_rate_bls",
    ascending=True
)

# Create the bar chart
plt.figure(figsize=(10, 6))

plt.barh(
    top_10_unemployment["county_label"],
    top_10_unemployment["unemployment_rate_bls"]
)

# Add title and labels
plt.title("Top 10 Kansas Counties by Unemployment Rate (2024)")
plt.xlabel("Unemployment Rate (%)")
plt.ylabel("County")

# Make the layout cleaner
plt.tight_layout()

# Save the chart
output_file = "outputs/charts/top_10_unemployment.png"
plt.savefig(output_file, dpi=300)

# Display the chart
plt.show()

print("Saved:", output_file)

# Find the 10 counties with the highest unemployment rates
top_10_unemployment = df.nlargest(
    10,
    "unemployment_rate_bls"
).copy()

# Use shorter county names for the chart
top_10_unemployment["county_label"] = (
    top_10_unemployment["county_name_census"]
    .str.replace(" County, Kansas", "", regex=False)
)

# Sort for a horizontal bar chart
top_10_unemployment = top_10_unemployment.sort_values(
    "unemployment_rate_bls",
    ascending=True
)

# Create the bar chart
plt.figure(figsize=(10, 6))

plt.barh(
    top_10_unemployment["county_label"],
    top_10_unemployment["unemployment_rate_bls"]
)

# Add title and labels
plt.title("Top 10 Kansas Counties by Unemployment Rate (2024)")
plt.xlabel("Unemployment Rate (%)")
plt.ylabel("County")

# Make the layout cleaner
plt.tight_layout()

# Save the chart
output_file = "outputs/charts/top_10_unemployment.png"
plt.savefig(output_file, dpi=300)

# Display the chart
plt.show()

print("Saved:", output_file)

