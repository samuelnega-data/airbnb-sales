# Airbnb Dataset Analysis 

## Overview
I conducted an in-depth analysis of Airbnb data, exploring various columns such as neighborhoods, prices, room types, and bed configurations. Using Python, I not only performed the analysis but also created insightful visualizations utilizing Seaborn and Matplotlib. Through this comprehensive examination, I uncovered several key insights, which I have presented in detail.

### Importing libraries  
```sql
-- Total cases in the world vs total deaths in the world
SELECT SUM(new_cases) AS TotalCases, SUM(new_deaths) AS TotalDeaths, SUM(new_deaths) / SUM(new_cases) * 100 AS DeathPercentage
FROM covidDeaths
WHERE continent IS NOT NULL
ORDER BY 1, 2;
```
