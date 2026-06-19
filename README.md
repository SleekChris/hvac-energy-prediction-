# hvac-energy-prediction-

# HVAC Chiller Energy Consumption Prediction

## Overview
This project analyzes historical weather and HVAC chiller operational data from a commercial building to identify the key factors driving energy consumption, and builds a predictive model to forecast energy use based on those factors.

## Problem Statement

Ideally, Commercial Business owners should be able to anticipate how much energy is going to be consumed in the future, due to outside temperatures, humidity, and wind speed.

Unfortunately, building owners can't predict how much energy consumption there will be in future events, due to the fact that they have no model that uses past data to forecast the future, nor a system that tracks the weather relationally with the energy consumption decision.

This is a significant problem because chilling HVAC systems run inefficiently, since nobody can predict or prepare for the upcoming weather demand, which results in high air conditioning/cooling bills that the Commercial Building owner may hand down to tenants.

Here are some of the solutions that I came up with that can help solve this issue, costing Commercial Building owners thousands of dollars annually:

1. Build a predictive model from raw historical weather and HVAC operational data to relay the estimated energy consumption ahead of time.
2. Add an alert system that notifies the Commercial Building owner when a prediction shows an increase in cooling energy usage.
3. Provide Commercial Building owners with a detailed breakdown of predicted versus actual energy costs, so that tenants can feel confident their billing is fair and accurate.
4. Use the predictive cooling system as a tangible data point to show to the Building energy provider to negotiate better rates, due to a proven track record of showing exemplary energy efficiency.

## Dataset
- **Source:** [Chiller Energy Data on Kaggle](https://www.kaggle.com/datasets/chillerenergy/chiller-energy-data)
- **Location:** Commercial building in Singapore
- **Time period:** 08/18/2019 – 06/01/2020
- **Rows:** 13,615 (after removing outliers/missing values)

### Attributes
| Column | Description |
|---|---|
| Local Time | Timestamp of the reading (GMT+8h) |
| Chilled Water Rate (L/sec) | Flow rate of chilled water through the system |
| Cooling Water Temperature (C) | Temperature of the cooling water |
| Building Load (RT) | Cooling demand on the building |
| Chiller Energy Consumption (kWh) | **Target variable** — energy used by the chiller |
| Outside Temperature (F) | Outdoor air temperature |
| Dew Point (F) | Moisture-related temperature measure |
| Humidity (%) | Outdoor humidity level |
| Wind Speed (mph) | Outdoor wind speed |
| Pressure (in) | Atmospheric pressure |

## Tools Used
- Python
- Pandas
- VS Code

## Skills Demonstrated
This project translates coursework from an AI Data Specialist Associate's degree (Data Modeling, Intro to SQL, Data Visualization, AI in Business) into a real-world application:

| Skill | How it's applied here |
|---|---|
| Data Modeling | Identifying entities, target variable, and feature relationships; building a conceptual model |
| Data Wrangling | Loading raw CSV data with Pandas, checking for missing values, generating summary statistics |
| Problem Definition | Writing a structured problem statement (ideal → actual → impact → solutions) |
| Technical Troubleshooting | Debugging environment setup, file path errors, and library installation issues |
| Data Visualization | *(in progress)* — charting relationships between weather and energy consumption |
| SQL | *(not yet applied — planned for querying/aggregating the dataset)* |
| Predictive Modeling | *(in progress)* — building a model to forecast energy consumption |

## Project Structure
```
hvac-energy-prediction/
├── README.md
├── data/
│   └── HVAC Energy Data.csv
├── notebooks/
│   └── hvac.py
├── docs/
│   └── conceptual_model.png
└── outputs/
    └── hvac_summary.xlsx
```

## Status
- [x] Dataset sourced and loaded
- [x] Data cleaned and validated (no missing values)
- [x] Summary statistics generated
- [x] Problem statement written
- [ ] Conceptual model built
- [ ] Data visualized
- [ ] SQL queries applied
- [ ] Predictive model built and evaluated

## Author
SleekChris
