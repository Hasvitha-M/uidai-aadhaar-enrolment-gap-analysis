# UIDAI Aadhaar Enrolment Gap Analysis – Data Hackathon 2026

## Project Overview
This project was developed as part of the **UIDAI Data Hackathon 2026**.  
The goal of the project was to build a **data-driven decision support framework** to identify **regional and age-wise gaps in Aadhaar enrolment across India**.

Aadhaar is the primary digital identity used to access welfare programs, government services, and digital governance. However, enrolment rates vary across **regions, districts, age groups, and time periods**.

This project converts aggregated Aadhaar enrolment data into **actionable insights** to support administrative decision-making and targeted enrolment initiatives.


## Problem Statement

Although Aadhaar enrolment is widely adopted, registration rates vary significantly across **regions, age groups, and time periods**.

Some districts and demographic groups remain **under-enrolled**, which may limit access to welfare programs and digital governance services.

Existing administrative analysis often relies on **aggregated statistics**, which makes it difficult to:

- Identify district-level enrolment gaps
- Understand enrolment differences across age groups
- Detect temporal patterns in enrolment activity

This project addresses this gap by developing a **data-driven analytical framework** to identify underserved regions and support evidence-based decision-making.


## Approach

The project follows a structured analytical workflow:

1. Consolidated enrolment data from multiple datasets.
2. Analyzed enrolment distribution across **states, districts, age groups, and time periods**.
3. Identified **low-enrolment districts** requiring administrative attention.
4. Examined **monthly enrolment trends** to identify patterns over time.
5. Developed an **interactive Power BI dashboard** to present insights clearly.

The goal is to transform raw enrolment data into **actionable insights for policy planning and targeted enrolment campaigns**.


## Dataset

**Dataset:** Aadhaar Enrolment Dataset (provided by UIDAI)

The dataset was provided as three CSV files:

```
api_data_aadhar_enrolment_0_500000.csv
api_data_aadhar_enrolment_500000_1000000.csv
api_data_aadhar_enrolment_1000000_1006029.csv
```

These files were combined into a **single dataset containing more than 1 million records**.

### Key Columns Used

- `date` – Date of enrolment  
- `state` – State name  
- `district` – District name  
- `pincode` – PIN code  
- `age_0_5` – Enrolments for age group 0–5  
- `age_5_17` – Enrolments for age group 5–17  
- `age_18_greater` – Enrolments for age group 18+  
- `total_enrolment` – Total enrolments per record (derived field)

⚠️ **Dataset Privacy Notice**

Due to UIDAI data-sharing guidelines, the dataset used in this project **cannot be publicly shared**.  
This repository includes only the **analysis methodology and dashboard explanation**.


## Methodology

### Data Cleaning and Preprocessing

- Combined the three CSV datasets using **Python**.
- Converted date fields into **datetime format**.
- Verified data types for numerical and categorical columns.
- Checked for **missing values and data consistency**.

### Feature Engineering

A new derived field was created:

```
total_enrolment = age_0_5 + age_5_17 + age_18_greater
```

This allowed the calculation of **total enrolments per record**.


## Data Aggregation

Enrolment data was aggregated at multiple levels:

- **State level**
- **District level**
- **Age-group level**
- **Monthly trends**

Power BI **DAX measures** were created to calculate:

- Total enrolments
- Child enrolments
- Youth enrolments
- Adult enrolments


## Filtering and Ranking

To identify underserved areas:

- **Top-N filtering** was applied to identify **low-enrolment districts**.
- Filter interactions were configured to maintain meaningful aggregation across time.


## Dashboard Visualizations

The final Power BI dashboard includes:

### KPI Cards
- Total Aadhaar enrolments
- Age-group-wise enrolments

### Age-wise Distribution
Comparison of enrolments across:

- Age 0–5
- Age 5–17
- Age 18+

### Monthly Enrolment Trend
Time-series visualization of enrolment activity over time.

### State-wise Enrolment Analysis
Comparison of enrolment volumes across different states.

### Low Enrolment Districts Table
Identification of districts requiring targeted enrolment interventions.


## Types of Analysis Performed

### Univariate Analysis
- Total Aadhaar enrolments across the dataset
- Age-wise enrolment distribution

### Bivariate Analysis
- State-wise enrolment comparison
- Monthly enrolment trends

### Trivariate Analysis
- District-level enrolment analysis across states and time
- Identification of priority districts based on enrolment levels


## Key Insights

- Aadhaar enrolment is **unevenly distributed across states**.
- Enrolment among **children aged 0–5 is significantly lower** compared to adults.
- Monthly enrolment data shows **seasonal spikes**, indicating periods of higher enrolment activity.
- Several districts consistently show **low enrolment levels**, highlighting priority areas for intervention.


## Policy Recommendations

Based on the analysis, the following actions are recommended:

1. **Targeted District Outreach**  
   Deploy mobile enrolment units in districts with consistently low enrolment.

2. **Child Enrolment Awareness Campaigns**  
   Promote awareness among parents to increase enrolment for children aged 0–5.

3. **Seasonal Resource Planning**  
   Allocate staff and infrastructure during peak enrolment periods.

4. **Continuous Monitoring Dashboard**  
   Use the dashboard as a monitoring system for evaluating enrolment progress.


## Conclusion

This project demonstrates how Aadhaar enrolment data can be transformed into a **decision-support framework**.

By integrating **geographic, demographic, and temporal analysis**, the system helps administrators:

- Identify under-enrolled districts
- Detect age-group enrolment gaps
- Support targeted enrolment campaigns

The interactive dashboard enables **evidence-based administrative planning** and improved Aadhaar coverage.


## Future Scope

The framework can be expanded by:

- Integrating demographic update and biometric datasets
- Incorporating socio-economic indicators
- Developing predictive models for enrolment demand
- Building automated monitoring dashboards

These enhancements would support **scalable data-driven governance**.


## Tools Used

- Python (Data Cleaning & Aggregation)
- Power BI Desktop (Visualization & Dashboard)

