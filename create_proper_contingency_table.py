#!/usr/bin/env python3
"""
Create Proper Contingency Table for Correspondence Analysis

Transforms user-visit data into Airlines × User_Types contingency table
which is appropriate for correspondence analysis.
"""

import pandas as pd
import numpy as np

def create_airline_usertype_table(filename: str = 'synthetic_airline_visits.csv') -> pd.DataFrame:
    """
    Create Airlines × User_Types contingency table from synthetic data
    """
    print(f"Creating Airlines × User_Types contingency table...")
    print(f"Loading data from '{filename}'...")
    
    try:
        # Load the full dataset with user_type information
        df = pd.read_csv(filename)
        print(f"Loaded {len(df):,} user sessions")
        
        # Get airline and user type columns
        airline_cols = [col for col in df.columns if col not in ['user_id', 'user_type']]
        user_types = df['user_type'].unique()
        
        print(f"Airlines: {airline_cols}")
        print(f"User types: {list(user_types)}")
        
        # Create contingency table: Airlines × User_Types
        contingency_table = pd.DataFrame(
            index=airline_cols,
            columns=sorted(user_types),
            data=0
        )
        
        # Fill the contingency table
        print("\nFilling contingency table...")
        for user_type in user_types:
            user_type_data = df[df['user_type'] == user_type]
            
            for airline in airline_cols:
                # Count users of this type who visited this airline
                visits = (user_type_data[airline] == 1).sum()
                contingency_table.loc[airline, user_type] = visits
        
        print(f"\nContingency table created:")
        print(contingency_table)
        
        # Print statistics
        print(f"\nContingency Table Statistics:")
        print(f"Shape: {contingency_table.shape}")
        print(f"Total entries: {contingency_table.sum().sum():,}")
        
        print(f"\nRow totals (airline visits):")
        row_totals = contingency_table.sum(axis=1).sort_values(ascending=False)
        for airline, total in row_totals.items():
            print(f"  {airline.replace('_', ' ')}: {total:,}")
        
        print(f"\nColumn totals (user type visits):")
        col_totals = contingency_table.sum(axis=0).sort_values(ascending=False)
        for user_type, total in col_totals.items():
            print(f"  {user_type.replace('_', ' ')}: {total:,}")
        
        # Check for low frequencies (CA works better with reasonable cell counts)
        min_count = contingency_table.min().min()
        print(f"\nMinimum cell count: {min_count}")
        if min_count < 5:
            print("⚠️  Warning: Some cells have very low counts (<5), which may affect CA quality")
        
        return contingency_table
        
    except FileNotFoundError:
        print(f"Error: {filename} not found. Please run generate_airline_data.py first.")
        raise

def create_alternative_tables(df_original: pd.DataFrame) -> dict:
    """
    Create alternative contingency tables for comparison
    """
    print(f"\n{'='*60}")
    print("CREATING ALTERNATIVE CONTINGENCY TABLES")
    print("="*60)
    
    airline_cols = [col for col in df_original.columns if col not in ['user_id', 'user_type']]
    
    # 1. Airlines × Number_of_visits (1, 2, 3, 4, 5+ airlines visited)
    print("\n1. Airlines × Visit_Pattern table...")
    visit_patterns = []
    for _, user in df_original.iterrows():
        num_visits = user[airline_cols].sum()
        if num_visits == 1:
            pattern = 'single_airline'
        elif num_visits == 2:
            pattern = 'two_airlines'
        elif num_visits == 3:
            pattern = 'three_airlines'
        elif num_visits >= 4:
            pattern = 'multi_airline'
        else:
            pattern = 'no_visits'
        visit_patterns.append(pattern)
    
    df_with_patterns = df_original.copy()
    df_with_patterns['visit_pattern'] = visit_patterns
    
    # Create Airlines × Visit_Pattern contingency table
    visit_pattern_table = pd.DataFrame(
        index=airline_cols,
        columns=sorted(df_with_patterns['visit_pattern'].unique()),
        data=0
    )
    
    for pattern in df_with_patterns['visit_pattern'].unique():
        pattern_data = df_with_patterns[df_with_patterns['visit_pattern'] == pattern]
        for airline in airline_cols:
            visits = (pattern_data[airline] == 1).sum()
            visit_pattern_table.loc[airline, pattern] = visits
    
    print(visit_pattern_table)
    
    # 2. Airlines × Geographic_preference (based on airline origins)
    print("\n2. Airlines × Geographic_Preference table...")
    
    # Define geographic preferences based on airline combinations
    geo_preferences = []
    for _, user in df_original.iterrows():
        uk_carriers = user[['British_Airways', 'Virgin_Atlantic']].sum()
        eu_carriers = user[['Lufthansa', 'Air_France']].sum()
        budget = user['Ryanair']
        
        if uk_carriers > 0 and eu_carriers == 0 and budget == 0:
            geo_pref = 'UK_focused'
        elif eu_carriers > 0 and uk_carriers == 0 and budget == 0:
            geo_pref = 'EU_focused'
        elif budget > 0 and uk_carriers == 0 and eu_carriers == 0:
            geo_pref = 'Budget_focused'
        elif uk_carriers > 0 and eu_carriers > 0:
            geo_pref = 'Pan_European'
        elif budget > 0 and (uk_carriers > 0 or eu_carriers > 0):
            geo_pref = 'Mixed_Premium_Budget'
        else:
            geo_pref = 'No_clear_preference'
        
        geo_preferences.append(geo_pref)
    
    df_with_geo = df_original.copy()
    df_with_geo['geo_preference'] = geo_preferences
    
    geo_table = pd.DataFrame(
        index=airline_cols,
        columns=sorted(df_with_geo['geo_preference'].unique()),
        data=0
    )
    
    for geo_pref in df_with_geo['geo_preference'].unique():
        geo_data = df_with_geo[df_with_geo['geo_preference'] == geo_pref]
        for airline in airline_cols:
            visits = (geo_data[airline] == 1).sum()
            geo_table.loc[airline, geo_pref] = visits
    
    print(geo_table)
    
    return {
        'visit_pattern': visit_pattern_table,
        'geographic': geo_table
    }

def save_contingency_tables(main_table: pd.DataFrame, alt_tables: dict):
    """Save all contingency tables"""
    print(f"\n{'='*60}")
    print("SAVING CONTINGENCY TABLES")
    print("="*60)
    
    # Save main table
    main_filename = 'airline_usertype_contingency.csv'
    main_table.to_csv(main_filename)
    print(f"✅ Main table saved: {main_filename}")
    
    # Save alternative tables
    for name, table in alt_tables.items():
        filename = f'airline_{name}_contingency.csv'
        table.to_csv(filename)
        print(f"✅ Alternative table saved: {filename}")
    
    print(f"\nRecommendation: Use 'airline_usertype_contingency.csv' for correspondence analysis")
    print("This table has Airlines as rows and User_Types as columns - ideal for CA!")

def main():
    """Main function to create proper contingency tables"""
    print("PROPER CONTINGENCY TABLE CREATION")
    print("=" * 50)
    print("Creating Airlines × User_Types table for correspondence analysis")
    print("(This is the correct format, not Airlines × Airlines)")
    print()
    
    # Create main Airlines × User_Types table
    main_table = create_airline_usertype_table()
    
    # Load original data for alternatives
    df_original = pd.read_csv('synthetic_airline_visits.csv')
    alt_tables = create_alternative_tables(df_original)
    
    # Save all tables
    save_contingency_tables(main_table, alt_tables)
    
    print(f"\n{'='*60}")
    print("✅ PROPER CONTINGENCY TABLES CREATED!")
    print("Ready for meaningful correspondence analysis.")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()