# Correspondence Analysis Example 2025

A modern Python implementation of correspondence analysis for analyzing contingency tables, demonstrating relationships between categorical variables through dimensional reduction and visualization.

## What is Correspondence Analysis?

Correspondence Analysis (CA) is a statistical technique that reveals relationships in contingency tables by:
- Transforming the table into a low-dimensional space
- Preserving chi-square distances between categories  
- Creating interpretable visualizations showing associations between row and column variables

This example analyzes cross-visitation patterns between energy company websites, showing which brands have similar visitor overlap patterns.

## Features

- **Modern Python Stack**: Uses Prince library with scikit-learn compatible API
- **Complete Workflow**: Data loading, analysis, visualization, and interpretation
- **Production Ready**: Robust error handling and configurable parameters
- **Mathematical Rigor**: Proper eigenvalue decomposition and coordinate calculation

## Quick Start

```bash
# Clone and setup
git clone https://github.com/modha/correspondence-example-2025.git
cd correspondence-example-2025

# Install dependencies with uv (recommended)
uv sync

# Run the analysis
uv run correspondence_demo.py
```

Or with pip:
```bash
pip install prince pandas matplotlib seaborn
python correspondence_demo.py
```

## Usage

The main script analyzes the included energy company dataset:

```python
from correspondence_demo import perform_correspondence_analysis, plot_ca_biplot

# Load your contingency table
data, sizes = load_data("your_data.csv")

# Perform correspondence analysis
ca = perform_correspondence_analysis(data)

# Create visualization
plot_ca_biplot(ca, data, sizes)
```

## Data Format

Your CSV should have:
- **First column**: Row labels (category names)
- **Remaining columns**: Numeric contingency table values
- **Optional 'size' column**: For proportional point sizing

Example structure:
```csv
Brand,website1.com,website2.com,website3.com,size
brand_a,1500,200,100,10
brand_b,300,800,150,5
brand_c,100,150,600,3
```

## Results

The analysis produces:
- **Eigenvalues**: Variance explained by each dimension
- **Biplot visualization**: Shows relationships between categories
- **Coordinates**: Numerical positions for further analysis
- **Interpretable output**: Clear statistical summaries

Example output:
```
Eigenvalues (Variance explained):
[0.425  0.3947]

Row contributions to first dimension:
eonenergy.com          1.221
edfenergy.com          0.136
makeitcheaper.com     -0.008
...
```

## Dependencies

- **prince**: Correspondence analysis implementation
- **pandas**: Data manipulation
- **matplotlib**: Plotting
- **numpy**: Numerical operations
- **seaborn**: Enhanced visualizations (optional)

## Mathematical Background

This implementation:
1. Standardizes contingency table residuals
2. Performs SVD decomposition 
3. Extracts principal coordinates
4. Preserves chi-square distances
5. Creates interpretable low-dimensional representation

The algorithm is mathematically equivalent to R's FactoMineR package but optimized for Python data science workflows.

## License

MIT License - feel free to use and modify for your own projects.

## Contributing

Issues and pull requests welcome! This is intended as both a learning resource and production-ready tool.