# Correspondence Analysis Example 2025

So this is a toy repo to illustrate a cheap hack - taking tables that can be interpreted as some measure of closeness/distance between entities such as brands - and reducing that to a two dimensional map. 

## What This Demonstrates

**Correspondence Analysis (CA)** reveals hidden relationships in contingency tables by mapping categories into a low-dimensional space that preserves chi-square distances. Perfect for market research, survey analysis, and categorical data exploration.

## Examplsa

There are three examples here - two from real data and one synthetic. The code to generate the synthetic data is also is the repo to give you a sense of the end to end process. 


1. **Energy Company Cross-Visitation** - Website overlap patterns (42.5% + 39.5% variance)
2. **Categorical Supplier Analysis** - Business relationship mapping (44.9% + 34.1% variance)  
3. **🆕 Synthetic Airline Market Segmentation** - **31.19% + 8.55% = 39.74% variance**

### Market Insights baked in
In the simulated airline data we bake in...

- **Budget vs Premium**: Clear separation between Ryanair and traditional carriers
- **Geographic Preferences**: UK business (BA/Virgin) vs European business (Lufthansa/Air France)
- **User Behavior**: Realistic segmentation with zero crossover between budget-conscious and business travelers


## Quick Start

```bash
# Clone and run
git clone https://github.com/spm1001/correspondence-example-2025.git
cd correspondence-example-2025
uv sync
uv run correspondence_demo.py  # Runs all three analyses
```

**Individual analyses:**
```bash
uv run correspondence_demo.py data.csv                           # Energy companies
uv run correspondence_demo.py co_occurrence_cat.csv             # Suppliers  
uv run correspondence_demo.py airline_usertype_contingency.csv  # Airlines (39.74% variance!)
```

## Example output

- `data_correspondence_analysis.png` - Energy market analysis
- `co_occurrence_cat_correspondence_analysis.png` - B2B supplier relationships
- `airline_usertype_contingency_correspondence_analysis.png` - **Market segmentation showcase**

### **Synthetic Data Pipeline:**
```bash
uv run generate_airline_data.py          # Create 100k realistic user sessions
uv run create_proper_contingency_table.py # Transform to CA-ready format
uv run correspondence_demo.py airline_usertype_contingency.csv # Analyze
```

**Mathematical stuff:**
- SVD decomposition of standardized residuals
- Chi-square distance preservation  
- Proper eigenvalue/coordinate calculations
- Equivalent to R's FactoMineR but optimized for Python
