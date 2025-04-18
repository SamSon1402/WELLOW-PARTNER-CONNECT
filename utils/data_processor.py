import pandas as pd

def load_wellow_data():
    """Load Wellow locations data"""
    try:
        return pd.read_csv('data/wellow_locations.csv')
    except FileNotFoundError:
        print("Wellow locations data file not found. Run generate_data.py first.")
        return pd.DataFrame()

def load_partners_data():
    """Load partners data"""
    try:
        return pd.read_csv('data/partners.csv')
    except FileNotFoundError:
        print("Partners data file not found. Run generate_data.py first.")
        return pd.DataFrame()

def filter_partners(partners_df, selected_types=None, selected_statuses=None, selected_values=None):
    """Filter partners based on selected criteria"""
    filtered_df = partners_df
    
    if selected_types and len(selected_types) > 0:
        filtered_df = filtered_df[filtered_df['PartnerType'].isin(selected_types)]
        
    if selected_statuses and len(selected_statuses) > 0:
        filtered_df = filtered_df[filtered_df['ContactStatus'].isin(selected_statuses)]
        
    if selected_values and len(selected_values) > 0:
        filtered_df = filtered_df[filtered_df['PotentialValue'].isin(selected_values)]
        
    return filtered_df