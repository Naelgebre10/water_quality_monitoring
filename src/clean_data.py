def clean_data(df):
    """
    Clean the dataset by handling missing or invalid values.
    Replaces missing pH and turbidity values with -1 (indicating invalid data).
    Args:
        df (pd.DataFrame): Original DataFrame.
    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    df = df.copy()
    df['ph'] = df['ph'].fillna(-1)
    df['turbidity'] = df['turbidity'].fillna(-1)
    return df
