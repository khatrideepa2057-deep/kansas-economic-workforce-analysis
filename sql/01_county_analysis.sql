-- ============================================================
-- Kansas Economic and Workforce Trends Analysis
-- County-Level Economic Analysis, 2024
-- Sources: U.S. Census Bureau ACS and BLS LAUS
-- ============================================================


-- ============================================================
-- Query 1: Counties with the highest unemployment rates
-- Purpose: Identify Kansas counties experiencing the highest
-- unemployment rates in 2024.
-- ============================================================

SELECT
    county_name,
    unemployment_rate
FROM kansas_county_economic_data
ORDER BY unemployment_rate DESC, county_name ASC
LIMIT 10;


-- ============================================================
-- Query 2: Counties with above-average unemployment and poverty
-- Purpose: Identify counties experiencing both higher-than-average
-- unemployment and higher-than-average poverty.
-- ============================================================

SELECT
    county_name,
    unemployment_rate,
    poverty_rate
FROM kansas_county_economic_data
WHERE unemployment_rate > (
    SELECT AVG(unemployment_rate)
    FROM kansas_county_economic_data
)
AND poverty_rate > (
    SELECT AVG(poverty_rate)
    FROM kansas_county_economic_data
)
ORDER BY unemployment_rate DESC, poverty_rate DESC;


-- ============================================================
-- Query 3: Counties with the lowest labor-force participation
-- Purpose: Identify counties with the lowest share of adults
-- participating in the labor force.
-- ============================================================

SELECT
    county_name,
    labor_force_participation_rate,
    unemployment_rate,
    poverty_rate
FROM kansas_county_economic_data
ORDER BY labor_force_participation_rate ASC, county_name ASC
LIMIT 10;


-- ============================================================
-- Query 4: Highest educational attainment and household income
-- Purpose: Compare counties with the highest bachelor's-or-higher
-- attainment rates with their median household incomes.
-- ============================================================

SELECT
    county_name,
    bachelors_or_higher_rate,
    median_household_income
FROM kansas_county_economic_data
ORDER BY bachelors_or_higher_rate DESC,
         median_household_income DESC
LIMIT 10;
