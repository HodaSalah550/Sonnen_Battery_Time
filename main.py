=import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def clean_data(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    df = df.dropna(subset=['timestamp'])
    df['grid_purchase'] = pd.to_numeric(df['grid_purchase'], errors='coerce').fillna(0)
    df['grid_feedin'] = pd.to_numeric(df['grid_feedin'], errors='coerce').fillna(0)
    df.drop_duplicates(inplace=True)
    df['hour'] = df['timestamp'].dt.hour
    return df

def transform_data(df):
    hourly = df.groupby('hour')[['grid_purchase', 'grid_feedin']].sum().reset_index()
    max_hour = hourly.loc[hourly['grid_feedin'].idxmax(), 'hour']
    hourly['is_peak_feedin_hour'] = hourly['hour'] == max_hour
    return hourly

def save_data(df, output_file):
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_path = "input/measurements_coding_challenge.csv"
    output_path = "output/cleaned_battery_data.csv"

    df = load_data(input_path)
    df_clean = clean_data(df)
    df_transformed = transform_data(df_clean)
    save_data(df_transformed, output_path)

    print(f"Cleaned data saved to {output_path}")
