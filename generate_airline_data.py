#!/usr/bin/env python3
"""
Synthetic Airline Dataset Generator

Creates realistic user session data for 100,000 users visiting 5 airlines
with meaningful co-occurrence patterns based on user behavior types.
"""

import pandas as pd
import numpy as np
import random
from typing import Dict, List, Tuple

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Define airlines with realistic characteristics
AIRLINES = {
    'British_Airways': {
        'type': 'premium',
        'region': 'UK',
        'routes': 'long_haul',
        'base_probability': 0.15
    },
    'Virgin_Atlantic': {
        'type': 'premium', 
        'region': 'UK',
        'routes': 'long_haul',
        'base_probability': 0.12
    },
    'Lufthansa': {
        'type': 'premium',
        'region': 'Europe',
        'routes': 'long_haul',
        'base_probability': 0.13
    },
    'Air_France': {
        'type': 'premium',
        'region': 'Europe', 
        'routes': 'long_haul',
        'base_probability': 0.11
    },
    'Ryanair': {
        'type': 'budget',
        'region': 'Europe',
        'routes': 'short_haul',
        'base_probability': 0.20
    }
}

# User behavior types with STRONGLY differentiated preferences  
USER_TYPES = {
    'business_uk': {
        'weight': 0.22,
        'preferences': {
            'British_Airways': 0.55,      # VERY strong preference
            'Virgin_Atlantic': 0.35,      # Strong secondary preference
            'Lufthansa': 0.08,           # Minimal consideration
            'Air_France': 0.02,          # Almost never
            'Ryanair': 0.00              # Never for business UK
        },
        'avg_visits': 2.2,  # Focus on fewer, premium options
        'cooccurrence_boost': {
            ('British_Airways', 'Virgin_Atlantic'): 5.0,  # Much stronger boost
        }
    },
    'business_european': {
        'weight': 0.18,
        'preferences': {
            'Lufthansa': 0.50,           # Dominant preference
            'Air_France': 0.40,          # Strong secondary
            'British_Airways': 0.08,     # Minimal
            'Virgin_Atlantic': 0.02,     # Almost never
            'Ryanair': 0.00              # Never for European business
        },
        'avg_visits': 2.1,
        'cooccurrence_boost': {
            ('Lufthansa', 'Air_France'): 5.0,
        }
    },
    'leisure_premium': {
        'weight': 0.25,
        'preferences': {
            'British_Airways': 0.30,
            'Virgin_Atlantic': 0.30, 
            'Lufthansa': 0.25,
            'Air_France': 0.15,
            'Ryanair': 0.00              # Premium leisure avoids budget
        },
        'avg_visits': 2.8,
        'cooccurrence_boost': {
            ('British_Airways', 'Virgin_Atlantic'): 3.5,
            ('Lufthansa', 'Air_France'): 3.0,
        }
    },
    'budget_conscious': {
        'weight': 0.25,
        'preferences': {
            'Ryanair': 0.75,             # OVERWHELMINGLY prefer Ryanair
            'British_Airways': 0.08,     # Rarely consider premium
            'Lufthansa': 0.07,
            'Air_France': 0.06,
            'Virgin_Atlantic': 0.04      # Least likely premium option
        },
        'avg_visits': 1.8,               # Budget users shop less
        'cooccurrence_boost': {
            ('Ryanair', 'British_Airways'): 2.0,  # When they do compare...
        }
    },
    'price_shopper': {
        'weight': 0.10,
        'preferences': {
            'Ryanair': 0.40,             # Start with budget but compare
            'British_Airways': 0.20,
            'Lufthansa': 0.18,
            'Air_France': 0.12,
            'Virgin_Atlantic': 0.10
        },
        'avg_visits': 3.5,  # Shop extensively
        'cooccurrence_boost': {
            ('Ryanair', 'British_Airways'): 4.0,    # Strong price comparison
            ('Ryanair', 'Lufthansa'): 3.5,
            ('British_Airways', 'Lufthansa'): 2.5,
        }
    }
}

def generate_user_type() -> str:
    """Randomly assign user type based on weights"""
    types = list(USER_TYPES.keys())
    weights = [USER_TYPES[t]['weight'] for t in types]
    return np.random.choice(types, p=weights)

def generate_user_visits(user_type: str) -> Dict[str, int]:
    """Generate airline visits for a single user based on their type"""
    user_profile = USER_TYPES[user_type]
    preferences = user_profile['preferences']
    avg_visits = user_profile['avg_visits']
    cooccurrence_boost = user_profile.get('cooccurrence_boost', {})
    
    # Determine number of airlines to visit (Poisson distribution around avg_visits)
    num_visits = max(1, int(np.random.poisson(avg_visits)))
    num_visits = min(num_visits, len(AIRLINES))  # Can't visit more airlines than exist
    
    # Initialize visit record
    visits = {airline: 0 for airline in AIRLINES.keys()}
    
    # First airline selection based on preferences
    first_airline = np.random.choice(list(preferences.keys()), p=list(preferences.values()))
    visits[first_airline] = 1
    visited_airlines = [first_airline]
    
    # Generate additional visits with co-occurrence boost
    for _ in range(num_visits - 1):
        # Calculate adjusted probabilities based on already visited airlines
        adjusted_probs = preferences.copy()
        
        # Apply co-occurrence boosts
        for visited in visited_airlines:
            for (a1, a2), boost in cooccurrence_boost.items():
                if visited == a1 and a2 not in visited_airlines:
                    adjusted_probs[a2] *= boost
                elif visited == a2 and a1 not in visited_airlines:
                    adjusted_probs[a1] *= boost
        
        # Remove already visited airlines
        for visited in visited_airlines:
            adjusted_probs[visited] = 0
        
        # Normalize probabilities
        total_prob = sum(adjusted_probs.values())
        if total_prob > 0:
            normalized_probs = {k: v/total_prob for k, v in adjusted_probs.items()}
            next_airline = np.random.choice(
                list(normalized_probs.keys()), 
                p=list(normalized_probs.values())
            )
            visits[next_airline] = 1
            visited_airlines.append(next_airline)
        
    return visits

def generate_synthetic_dataset(num_users: int = 100000) -> pd.DataFrame:
    """Generate complete synthetic dataset"""
    print(f"Generating synthetic airline visit data for {num_users:,} users...")
    
    # Generate data
    data_rows = []
    
    # Progress tracking
    checkpoint = num_users // 20  # Show progress every 5%
    
    for user_id in range(num_users):
        if user_id % checkpoint == 0:
            progress = (user_id / num_users) * 100
            print(f"Progress: {progress:.0f}% ({user_id:,}/{num_users:,} users)")
        
        # Generate user type and visits
        user_type = generate_user_type()
        visits = generate_user_visits(user_type)
        
        # Create row with user_id and visit data
        row = {'user_id': f'user_{user_id:06d}', 'user_type': user_type}
        row.update(visits)
        data_rows.append(row)
    
    print("Progress: 100% - Dataset generation complete!")
    
    # Convert to DataFrame
    df = pd.DataFrame(data_rows)
    
    # Print statistics
    print("\n" + "="*60)
    print("SYNTHETIC AIRLINE DATASET STATISTICS")
    print("="*60)
    
    # Overall statistics
    total_visits = df[list(AIRLINES.keys())].sum().sum()
    avg_visits_per_user = total_visits / num_users
    print(f"Total users: {num_users:,}")
    print(f"Total airline visits: {total_visits:,}")
    print(f"Average visits per user: {avg_visits_per_user:.2f}")
    
    # User type distribution
    print(f"\nUser type distribution:")
    user_type_counts = df['user_type'].value_counts()
    for user_type, count in user_type_counts.items():
        pct = (count / num_users) * 100
        print(f"  {user_type}: {count:,} ({pct:.1f}%)")
    
    # Airline visit statistics
    print(f"\nAirline visit counts:")
    for airline in AIRLINES.keys():
        visits = df[airline].sum()
        pct = (visits / total_visits) * 100
        print(f"  {airline}: {visits:,} ({pct:.1f}%)")
    
    # Co-occurrence statistics (sample)
    print(f"\nTop co-occurrence pairs:")
    cooccur_stats = []
    airlines_list = list(AIRLINES.keys())
    for i, airline1 in enumerate(airlines_list):
        for airline2 in airlines_list[i+1:]:
            cooccur = ((df[airline1] == 1) & (df[airline2] == 1)).sum()
            cooccur_stats.append((airline1, airline2, cooccur))
    
    cooccur_stats.sort(key=lambda x: x[2], reverse=True)
    for airline1, airline2, count in cooccur_stats[:5]:
        print(f"  {airline1} & {airline2}: {count:,}")
    
    return df

def save_dataset(df: pd.DataFrame, filename: str = 'synthetic_airline_visits.csv'):
    """Save dataset to CSV file"""
    # Save with user metadata
    print(f"\nSaving dataset to '{filename}'...")
    df.to_csv(filename, index=False)
    print(f"Dataset saved successfully!")
    
    # Also save a version without user_type for analysis
    analysis_df = df.drop('user_type', axis=1)
    analysis_filename = filename.replace('.csv', '_for_analysis.csv')
    analysis_df.to_csv(analysis_filename, index=False)
    print(f"Analysis version saved to '{analysis_filename}'")

def main():
    """Main function to generate and save synthetic airline dataset"""
    print("SYNTHETIC AIRLINE DATASET GENERATOR")
    print("=" * 50)
    print("Creating realistic user visit patterns for 5 airlines:")
    print("- British Airways (Premium, UK)")
    print("- Virgin Atlantic (Premium, UK)")  
    print("- Lufthansa (Premium, Europe)")
    print("- Air France (Premium, Europe)")
    print("- Ryanair (Budget, Europe)")
    print()
    
    # Generate dataset
    df = generate_synthetic_dataset(num_users=100000)
    
    # Save dataset
    save_dataset(df)
    
    print(f"\n{'='*60}")
    print("DATASET GENERATION COMPLETE!")
    print("Ready for overlap table transformation and correspondence analysis.")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()