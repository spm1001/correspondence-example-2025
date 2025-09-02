#!/usr/bin/env python3
"""
Correspondence Analysis Demo

A modern Python implementation for analyzing contingency tables using
correspondence analysis, equivalent to R's FactoMineR package.

This example analyzes energy company website cross-visitation data.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from prince import CA

def load_data(filename="data.csv"):
    """Load and prepare data for correspondence analysis"""
    # Load data with first column as index (Brand names)
    data = pd.read_csv(filename, index_col=0)
    
    # Remove the 'size' column if it exists (used for point sizing in R)
    if 'size' in data.columns:
        sizes = data['size']
        data = data.drop('size', axis=1)
        return data, sizes
    
    return data, None

def perform_correspondence_analysis(data, n_components=2):
    """Perform correspondence analysis using Prince library"""
    
    # Initialize CA model
    ca = CA(
        n_components=n_components,
        n_iter=10,
        copy=True,
        check_input=True,
        engine='sklearn',
        random_state=42
    )
    
    # Fit the model
    ca = ca.fit(data)
    
    return ca

def plot_ca_biplot(ca, data, sizes=None, figsize=(10, 8)):
    """Create a biplot similar to R's fviz_ca_biplot"""
    
    # Get row and column coordinates
    row_coords = ca.row_coordinates(data)
    col_coords = ca.column_coordinates(data)
    
    # Convert to DataFrames if they're numpy arrays
    if not hasattr(row_coords, 'iloc'):
        row_coords = pd.DataFrame(row_coords, index=data.index)
    if not hasattr(col_coords, 'iloc'):
        col_coords = pd.DataFrame(col_coords, index=data.columns)
    
    # Create the plot
    plt.figure(figsize=figsize)
    
    # Plot column points (variables)
    plt.scatter(col_coords.iloc[:, 0], col_coords.iloc[:, 1], 
               c='red', marker='^', s=100, alpha=0.7, label='Variables')
    
    # Plot row points (observations) with optional sizing
    if sizes is not None:
        # Scale sizes for visualization
        scaled_sizes = sizes * 20  # Adjust scaling factor as needed
        plt.scatter(row_coords.iloc[:, 0], row_coords.iloc[:, 1], 
                   c='blue', s=scaled_sizes, alpha=0.7, label='Observations')
    else:
        plt.scatter(row_coords.iloc[:, 0], row_coords.iloc[:, 1], 
                   c='blue', s=100, alpha=0.7, label='Observations')
    
    # Add labels with offset to prevent overlap
    for i, txt in enumerate(row_coords.index):
        plt.annotate(txt, (row_coords.iloc[i, 0], row_coords.iloc[i, 1]), 
                    xytext=(5, 5), textcoords='offset points', fontsize=9)
    
    for i, txt in enumerate(col_coords.index):
        plt.annotate(txt, (col_coords.iloc[i, 0], col_coords.iloc[i, 1]), 
                    xytext=(5, 5), textcoords='offset points', fontsize=9, color='red')
    
    # Add axis lines
    plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)
    plt.axvline(x=0, color='black', linestyle='-', alpha=0.3)
    
    # Labels and formatting
    eigenvalues = ca.eigenvalues_
    if hasattr(eigenvalues, 'iloc'):
        plt.xlabel(f'Dimension 1 ({eigenvalues.iloc[0]:.1%} of variance)')
        plt.ylabel(f'Dimension 2 ({eigenvalues.iloc[1]:.1%} of variance)')
    else:
        plt.xlabel(f'Dimension 1 ({eigenvalues[0]:.1%} of variance)')
        plt.ylabel(f'Dimension 2 ({eigenvalues[1]:.1%} of variance)')
    plt.title('Correspondence Analysis Biplot')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    # Save plot instead of showing (for headless operation)
    plt.savefig('correspondence_plot.png', dpi=300, bbox_inches='tight')
    print("Plot saved as 'correspondence_plot.png'")
    plt.close()

def print_eigenvalues(ca):
    """Print eigenvalues similar to R's get_eigenvalue output"""
    eigenvalues_df = ca.eigenvalues_
    print("Eigenvalues (Variance explained):")
    if hasattr(eigenvalues_df, 'round'):
        print(eigenvalues_df.round(4))
    else:
        print(np.round(eigenvalues_df, 4))
    print()

def main():
    """Main demonstration function"""
    print("Python Correspondence Analysis Demo")
    print("=" * 40)
    
    # Load data
    try:
        data, sizes = load_data()
        print(f"Loaded data with shape: {data.shape}")
        print(f"Row names (Brands): {list(data.index)}")
        print(f"Column names: {list(data.columns)}")
        print()
        
        # Perform correspondence analysis
        ca = perform_correspondence_analysis(data)
        
        # Print eigenvalues
        print_eigenvalues(ca)
        
        # Create biplot
        plot_ca_biplot(ca, data, sizes)
        
        # Additional analysis
        print("Row contributions to first dimension:")
        row_coords = ca.row_coordinates(data)
        if hasattr(row_coords, 'iloc'):
            print(row_coords.iloc[:, 0].sort_values(ascending=False).round(3))
        else:
            first_dim = pd.Series(row_coords[:, 0], index=data.index)
            print(first_dim.sort_values(ascending=False).round(3))
        
    except FileNotFoundError:
        print("Error: data.csv not found. Please ensure the data file is in the current directory.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()