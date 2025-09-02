# Correspondence Analysis Example 2025 🚀

**Professional-grade Python correspondence analysis** with **39.74% variance explained** - demonstrating clear market segmentation and user behavior patterns.

## 🎯 What This Demonstrates

**Correspondence Analysis (CA)** reveals hidden relationships in contingency tables by mapping categories into a low-dimensional space that preserves chi-square distances. Perfect for market research, survey analysis, and categorical data exploration.

## ⭐ Key Results

### Three Complete Analyses:
1. **Energy Company Cross-Visitation** - Website overlap patterns (42.5% + 39.5% variance)
2. **Categorical Supplier Analysis** - Business relationship mapping (44.9% + 34.1% variance)  
3. **🆕 Synthetic Airline Market Segmentation** - **31.19% + 8.55% = 39.74% variance**

### Market Insights Revealed:
- **Budget vs Premium**: Clear separation between Ryanair and traditional carriers
- **Geographic Preferences**: UK business (BA/Virgin) vs European business (Lufthansa/Air France)
- **User Behavior**: Realistic segmentation with zero crossover between budget-conscious and business travelers

## 🔥 Features

- **High-Variance Results**: Engineered synthetic data with strong, realistic relationships
- **Modern Visualizations**: Professional styling with clear category differentiation
- **Complete Workflow**: From synthetic data generation to final insights
- **Production Ready**: Robust code with comprehensive error handling

## ⚡ Quick Start

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

## 📊 What You Get

### **Three Professional Visualizations:**
- `data_correspondence_analysis.png` - Energy market analysis
- `co_occurrence_cat_correspondence_analysis.png` - B2B supplier relationships
- `airline_usertype_contingency_correspondence_analysis.png` - **Market segmentation showcase**

### **Synthetic Data Pipeline:**
```bash
uv run generate_airline_data.py          # Create 100k realistic user sessions
uv run create_proper_contingency_table.py # Transform to CA-ready format
uv run correspondence_demo.py airline_usertype_contingency.csv # Analyze
```

### **Key Outputs:**
- **High variance explained** (31-45% first dimension)
- **Clear market segments** with realistic behavioral patterns
- **Professional visualizations** suitable for presentations
- **Complete source code** for customization and learning

## 🧠 Why This Works

**Strong relationships create high variance explained:**
- **Business UK**: 55% prefer British Airways, 0% consider Ryanair
- **Budget Conscious**: 75% choose Ryanair, minimal premium consideration  
- **Geographic Segmentation**: UK carriers vs European carriers vs budget
- **Realistic Behavioral Patterns**: No unrealistic cross-category appeal

## 🔧 Technical Details

**Modern Python Stack:**
- `prince` - Correspondence analysis (scikit-learn compatible)
- `pandas` - Data manipulation and contingency tables
- `matplotlib + seaborn` - Professional visualizations
- `uv` - Fast, reliable dependency management

**Mathematical Rigor:**
- SVD decomposition of standardized residuals
- Chi-square distance preservation  
- Proper eigenvalue/coordinate calculations
- Equivalent to R's FactoMineR but optimized for Python

## 📚 Perfect For

- **Learning CA**: Complete workflow from data generation to insights
- **Market Research**: Realistic segmentation patterns and user behavior modeling
- **Academic Use**: High-variance results suitable for teaching statistical methods
- **Business Analysis**: Professional visualizations ready for presentations

---

**MIT License** • Contributions welcome • Built with [Claude Code](https://claude.ai/code)