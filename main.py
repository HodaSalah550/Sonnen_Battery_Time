import pandas as pd
from datetime import datetime

#Load the CSV file
def load_data(measurements_coding_challenge.csv):
    return pd.read_csv(measurements_coding_challenge.csv)

def clean_data(df):
    
    # i. Missing values: Replace missing values with appropriate default values (e. g. Null values)
    df.fillna({
        'grid_purchase': 0,
        'grid_feedin': 0
    }, inplace=True)
    
    
    # ii. Incorrect data types: Convert columns to their appropriate data types (e. g. integers).

    for col in ['grid_purchase', 'grid_feedin']:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
        
        
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    else:
        raise KeyError("Missing 'timestamp' column")



    # iii. Remove duplicates and corrupt values from the dataset
    
    df.drop_duplicates(inplace=True)
    #drop rows if timestamp is invalid 
    df.dropna(subset=['timestamp'], inplace=True)
    
    
    #Extract hour for next step
    df['hour'] = df['timestamp'].dt.hour

    return df


#After cleansing, calculate the total grid_purchase and grid_feedin over all batteries for each hour of the day

def transform_data(df):
    hourly_sum = df.groupby('hour')[['grid_purchase', 'grid_feedin']].sum().reset_index()

    # Find the hour with the highest grid_feedin
    highest_hour = hourly_sum.loc[hourly_sum['grid_feedin'].idxmax(), 'hour']
    
    # Add a column to your dataframe that indicates the hour with the highest grid_feedin of the day (e. g. a Boolean value
    hourly_sum['is_peak_feedin_hour'] = hourly_sum['hour'] == highest_hour

    return hourly_sum


# Write the transformed data to an output file in CSV format

def save_data(df, output_path):
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    input_file = "measurements_coding_challenge.csv"
    output_file = "battery_data.csv"

    df = load_data(input_file)
    df_clean = clean_data(df)
    df_transformed = transform_data(df_clean)
    save_data(df_transformed, output_file)

    print(f"Task complete. Output saved to {output_file}")
