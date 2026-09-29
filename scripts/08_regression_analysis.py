import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Load the final Kansas county dataset
file_path = "data/processed/kansas_economic_workforce_2024.csv"
df = pd.read_csv(file_path)

# Select variables for the regression analysis
regression_df = df[
    [
        "unemployment_rate_bls",
        "poverty_rate",
        "median_household_income",
        "bachelors_or_higher_rate",
        "labor_force_participation_rate"
    ]
].copy()

# Display the first 5 rows
print(regression_df.head())

# Check the number of observations and variables
print("\nDataset shape:", regression_df.shape)

# Check for missing values
print("\nMissing values:")
print(regression_df.isnull().sum())

# Define the dependent variable
# This is the outcome we want to explain
y = regression_df["unemployment_rate_bls"]

# Define the independent variables
# These are the factors we want to examine
X = regression_df[
    [
        "poverty_rate",
        "median_household_income",
        "bachelors_or_higher_rate",
        "labor_force_participation_rate"
    ]
]

# Add a constant to the regression model
X = sm.add_constant(X)

# Build the multiple linear regression model
model = sm.OLS(y, X).fit()

# Display the regression results
print("\nRegression Results:")
print(model.summary())

# Check multicollinearity using Variance Inflation Factor (VIF)
vif_data = pd.DataFrame()

vif_data["Variable"] = X.columns

vif_data["VIF"] = [
    variance_inflation_factor(X.values, i)
    for i in range(X.shape[1])
]

print("\nVariance Inflation Factor (VIF):")
print(vif_data)

