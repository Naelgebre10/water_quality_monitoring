import pandas as pd

def load_data(file_path):
    """
    Load sensor data from a CSV file into a pandas DataFrame.
    Args:
        file_path (str): Path to the CSV file.
    Returns:
        pd.DataFrame: Loaded data.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"✅ Data loaded successfully from {file_path}")
        return df
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        return pd.DataFrame()
