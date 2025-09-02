# CLAUDE.md - Agent Instructions

This document provides guidance to Claude Code when working on this correspondence analysis project.

## Project Context

This is a modern Python implementation of correspondence analysis, providing an alternative to R's FactoMineR package. The project demonstrates statistical analysis of contingency tables with emphasis on:

- Clean, production-ready code
- Mathematical accuracy and consistency
- Educational value for learning correspondence analysis
- Integration with modern Python data science tools

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

### Educational Focus
When explaining correspondence analysis concepts:
- **Intuitive Explanations**: Connect mathematical concepts to real-world interpretations
- **Step-by-Step Breakdown**: Show the transformation from contingency table to final visualization
- **Comparative Context**: Reference R implementations when helpful for users migrating from R
- **Visual Examples**: Always provide concrete examples with the energy company dataset

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

## Project-Specific Notes

### Data Format Expectations
The current implementation expects:
- CSV with first column as row labels
- Numeric contingency table in remaining columns  
- Optional 'size' column for point scaling
- No missing values (handle gracefully if present)

### Key Functions to Maintain
- `load_data()`: Robust CSV loading with validation
- `perform_correspondence_analysis()`: Core statistical computation
- `plot_ca_biplot()`: Primary visualization method
- `print_eigenvalues()`: Statistical summary output

### Performance Considerations
- The Prince library scales well to medium-sized tables (< 1000 x 1000)
- For larger tables, consider sparse matrix optimizations
- Matplotlib rendering can be slow; provide options for different backends

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

This project serves as both a practical tool and educational resource. Balance production-ready robustness with pedagogical clarity.