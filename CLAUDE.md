# CLAUDE.md - Agent Instructions

This document provides guidance to Claude Code when working on this **high-variance correspondence analysis project** that demonstrates professional-grade statistical analysis.

## Project Context

This is a **showcase-quality** Python implementation of correspondence analysis achieving **39.74% variance explained** through carefully engineered synthetic data. The project demonstrates:

- **Strong statistical relationships** with realistic market segmentation patterns
- **Production-ready code** suitable for business analysis and academic use  
- **Complete workflow** from synthetic data generation to professional visualizations
- **Modern Python ecosystem** integration (Prince, pandas, matplotlib, uv)

## Development Guidelines

### Code Quality Standards
- **Mathematical Rigor**: Ensure all statistical computations are mathematically correct
- **Error Handling**: Robust handling of edge cases (empty data, malformed input, etc.)
- **Documentation**: Clear docstrings explaining statistical concepts and implementation details
- **Modularity**: Functions should be reusable and testable independently

### Statistical Accuracy Requirements
- **Validation**: Always verify results match established statistical software (R's FactoMineR)
- **Eigenvalue Consistency**: Ensure eigenvalues sum correctly and represent proper variance decomposition
- **Coordinate Calculation**: Row and column coordinates must preserve chi-square distances
- **Visualization Accuracy**: Plots should represent the mathematical relationships faithfully

### Python Ecosystem Integration
- **Modern Tools**: Prefer `uv` for dependency management over pip when possible
- **Scientific Stack**: Leverage pandas, numpy, matplotlib, scikit-learn ecosystem
- **Library Selection**: Use Prince library for correspondence analysis (most mature Python implementation)
- **Type Safety**: Add type hints where appropriate for better code clarity

### Educational Focus & High-Variance Design
When working with this project's datasets:
- **Strong Relationships**: Maintain polarized user preferences (e.g., Business UK: 55% BA, 0% Ryanair)
- **Realistic Segmentation**: Ensure zero crossover between incompatible segments (business vs budget)
- **Clear Differentiation**: Avoid homogeneous distributions that reduce variance explained
- **Market Logic**: Geographic (UK vs EU), economic (budget vs premium), and behavioral patterns must align

**Variance Explained Targets:**
- **First Dimension**: Aim for 25-35% (indicates strong primary relationship)  
- **Second Dimension**: Target 8-15% (meaningful secondary pattern)
- **Total**: 35-45% is excellent for real-world data patterns

### Testing and Validation
- **Cross-Validation**: Compare outputs with known good results from R
- **Edge Cases**: Test with different table sizes, sparse matrices, edge cases
- **Reproducibility**: Ensure random seed control for consistent results
- **Performance**: Monitor execution time for large contingency tables

### Documentation Standards
- **README.md**: Should be accessible to both beginners and experienced practitioners
- **Code Comments**: Focus on "why" not "what" - explain statistical reasoning
- **Examples**: Provide both simple usage and advanced customization options
- **Mathematical Background**: Include references to academic sources when appropriate

### Common Pitfalls to Avoid
- **Coordinate Sign Ambiguity**: Correspondence analysis coordinates can be flipped; ensure consistency
- **Scaling Issues**: Be careful with different scaling approaches (symmetric vs. asymmetric)
- **Visualization Misleading**: Ensure axis labels correctly show variance explained
- **Memory Usage**: Large contingency tables can cause memory issues; handle gracefully

### Future Enhancement Areas
- **Multiple Correspondence Analysis (MCA)**: Extension for categorical data
- **Supplementary Elements**: Support for supplementary rows/columns
- **Interactive Visualizations**: Plotly integration for web-based exploration
- **Statistical Tests**: Confidence ellipses, contribution significance testing

## Project-Specific Success Patterns

### Synthetic Data Engineering Lessons
**What Creates High Variance (39.74% achieved):**
- **Extreme Preferences**: Business UK (55% BA, 0% Ryanair) vs Budget Conscious (75% Ryanair)
- **Zero Crossover**: Business segments never consider budget options
- **Geographic Clustering**: UK carriers vs European carriers with minimal overlap  
- **Enhanced Boost Factors**: Up to 5.0× for co-occurrence within segments

**What Reduces Variance (avoid):**
- Homogeneous distributions across categories
- Weak preference differences (e.g., 25% vs 20% vs 15%)
- Unrealistic cross-category appeal
- Too many visit patterns per user type

### Key Analyses Delivered
1. **Energy Companies**: 42.5% + 39.5% = 82% (real data)
2. **Categorical Suppliers**: 44.9% + 34.1% = 79% (real data)  
3. **🏆 Airline Segmentation**: 31.19% + 8.55% = 39.74% (engineered synthetic data)

### Essential Files & Functions  
- **`generate_airline_data.py`**: Creates 100k realistic user sessions with strong behavioral patterns
- **`create_proper_contingency_table.py`**: Transforms to Airlines × User_Types format
- **`correspondence_demo.py`**: Enhanced CA with modern visualizations
- **Three PNG outputs**: Professional-quality visualizations ready for presentations

## Maintenance Guidelines

### Version Compatibility
- Keep Prince library updated (currently using 0.16.1)
- Test with different Python versions (3.9+)
- Monitor scikit-learn compatibility (Prince dependency)

### Security Considerations  
- **Input Validation**: Sanitize file inputs to prevent injection attacks
- **Data Privacy**: This example uses public web traffic data - be mindful of sensitive datasets
- **Dependencies**: Regularly update dependencies for security patches

### Community Engagement
- **Issues**: Provide clear reproduction steps and expected vs. actual behavior
- **Pull Requests**: Ensure statistical correctness before code style
- **Documentation**: Prioritize mathematical clarity over code brevity

## 🎯 Project Achievement Summary

This project demonstrates **professional-grade correspondence analysis** with exceptional results:
- **4.7× variance improvement** (8.52% → 39.74%) through strategic synthetic data design
- **Three complete analyses** showcasing different data types and market scenarios  
- **Production-ready code** with modern Python ecosystem integration
- **Educational value** showing both technique and data engineering for strong CA results

**Key Success**: Proving that well-engineered synthetic data with realistic behavioral patterns can create **high-variance, interpretable correspondence analysis** suitable for business insights and academic demonstration.

Balance production-ready robustness with pedagogical clarity while maintaining the strong relationships that make this analysis compelling.