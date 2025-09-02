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

# Set modern styling
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")
plt.rcParams.update({
    'font.family': ['system-ui', 'DejaVu Sans', 'Arial', 'sans-serif'],
    'font.size': 11,
    'axes.linewidth': 0.8,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'grid.alpha': 0.3,
    'figure.facecolor': 'white'
})

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

def plot_ca_biplot(ca, data, sizes=None, figsize=(12, 9), output_file='correspondence_plot.png'):
    """Create a modern-styled biplot for correspondence analysis"""
    
    # Get row and column coordinates
    row_coords = ca.row_coordinates(data)
    col_coords = ca.column_coordinates(data)
    
    # Convert to DataFrames if they're numpy arrays
    if not hasattr(row_coords, 'iloc'):
        row_coords = pd.DataFrame(row_coords, index=data.index)
    if not hasattr(col_coords, 'iloc'):
        col_coords = pd.DataFrame(col_coords, index=data.columns)
    
    # Create the plot with modern styling
    fig, ax = plt.subplots(figsize=figsize, facecolor='white')
    ax.set_facecolor('#fafafa')
    
    # Modern color palette
    row_color = '#2E86AB'  # Ocean blue
    col_color = '#A23B72'  # Deep rose
    
    # Plot column points (variables) with modern styling
    scatter_cols = ax.scatter(col_coords.iloc[:, 0], col_coords.iloc[:, 1], 
                             c=col_color, marker='s', s=120, alpha=0.8, 
                             label='Variables', edgecolors='white', linewidth=1.5)
    
    # Plot row points (observations) with optional sizing
    if sizes is not None:
        # Scale sizes for visualization (more sophisticated scaling)
        size_min, size_max = 80, 300
        scaled_sizes = size_min + (sizes - sizes.min()) / (sizes.max() - sizes.min()) * (size_max - size_min)
        scatter_rows = ax.scatter(row_coords.iloc[:, 0], row_coords.iloc[:, 1], 
                                 c=row_color, s=scaled_sizes, alpha=0.8, 
                                 label='Observations', edgecolors='white', linewidth=1.5)
    else:
        scatter_rows = ax.scatter(row_coords.iloc[:, 0], row_coords.iloc[:, 1], 
                                 c=row_color, s=120, alpha=0.8, 
                                 label='Observations', edgecolors='white', linewidth=1.5)
    
    # Add labels with modern typography and smart positioning
    for i, txt in enumerate(row_coords.index):
        # Clean up label text (remove .com, .co.uk etc for readability)
        clean_txt = txt.replace('.co.uk', '').replace('.com', '').replace('.org.uk', '')
        ax.annotate(clean_txt, (row_coords.iloc[i, 0], row_coords.iloc[i, 1]), 
                   xytext=(8, 8), textcoords='offset points', 
                   fontsize=10, fontweight='500', color='#2c3e50',
                   bbox=dict(boxstyle="round,pad=0.3", facecolor='white', 
                            alpha=0.7, edgecolor='none'))
    
    for i, txt in enumerate(col_coords.index):
        # Clean up label text
        clean_txt = txt.replace('.co.uk', '').replace('.com', '').replace('.org.uk', '')
        ax.annotate(clean_txt, (col_coords.iloc[i, 0], col_coords.iloc[i, 1]), 
                   xytext=(8, 8), textcoords='offset points', 
                   fontsize=10, fontweight='500', color='#8e44ad',
                   bbox=dict(boxstyle="round,pad=0.3", facecolor='white', 
                            alpha=0.7, edgecolor='none'))
    
    # Add subtle axis lines
    ax.axhline(y=0, color='#bdc3c7', linestyle='-', alpha=0.6, linewidth=1)
    ax.axvline(x=0, color='#bdc3c7', linestyle='-', alpha=0.6, linewidth=1)
    
    # Modern labels and formatting
    eigenvalues = ca.eigenvalues_
    if hasattr(eigenvalues, 'iloc'):
        var1, var2 = eigenvalues.iloc[0], eigenvalues.iloc[1]
    else:
        var1, var2 = eigenvalues[0], eigenvalues[1]
    
    ax.set_xlabel(f'Dimension 1 ({var1:.1%} of variance)', fontsize=13, fontweight='600', color='#2c3e50')
    ax.set_ylabel(f'Dimension 2 ({var2:.1%} of variance)', fontsize=13, fontweight='600', color='#2c3e50')
    ax.set_title('Correspondence Analysis Biplot', fontsize=16, fontweight='700', 
                color='#2c3e50', pad=20)
    
    # Modern legend
    legend = ax.legend(loc='upper right', frameon=True, fancybox=True, shadow=False, 
                      fontsize=11, title_fontsize=12)
    legend.get_frame().set_facecolor('white')
    legend.get_frame().set_edgecolor('#ecf0f1')
    legend.get_frame().set_alpha(0.9)
    
    # Clean up grid
    ax.grid(True, alpha=0.2, linestyle='-', linewidth=0.5)
    ax.set_axisbelow(True)
    
    # Remove top and right spines for cleaner look
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#bdc3c7')
    ax.spines['bottom'].set_color('#bdc3c7')
    
    plt.tight_layout()
    
    # Save with high quality
    plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor='white', 
                edgecolor='none', pad_inches=0.2)
    print(f"Modern styled plot saved as '{output_file}'")
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

def main(filename="data.csv"):
    """Main demonstration function"""
    print(f"Python Correspondence Analysis Demo: {filename}")
    print("=" * 50)
    
    # Load data
    try:
        data, sizes = load_data(filename)
        print(f"Loaded data with shape: {data.shape}")
        print(f"Row names: {list(data.index)}")
        print(f"Column names: {list(data.columns)}")
        print()
        
        # Perform correspondence analysis
        ca = perform_correspondence_analysis(data)
        
        # Print eigenvalues
        print_eigenvalues(ca)
        
        # Create biplot with custom filename
        base_name = filename.replace('.csv', '')
        output_file = f'{base_name}_correspondence_analysis.png'
        plot_ca_biplot(ca, data, sizes, output_file=output_file)
        
        # Additional analysis
        print("Row contributions to first dimension:")
        row_coords = ca.row_coordinates(data)
        if hasattr(row_coords, 'iloc'):
            print(row_coords.iloc[:, 0].sort_values(ascending=False).round(3))
        else:
            first_dim = pd.Series(row_coords[:, 0], index=data.index)
            print(first_dim.sort_values(ascending=False).round(3))
        
    except FileNotFoundError:
        print(f"Error: {filename} not found. Please ensure the data file is in the current directory.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        # Run specific dataset
        main(sys.argv[1])
    else:
        # Run both datasets by default
        datasets = ["data.csv", "co_occurrence_cat.csv"]
        for dataset in datasets:
            try:
                main(dataset)
                print("\n" + "="*60 + "\n")
            except FileNotFoundError:
                print(f"Skipping {dataset} - file not found")
                continue