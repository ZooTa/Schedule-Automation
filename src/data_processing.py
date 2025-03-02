import pandas as pd
import logging
import os
from fuzzywuzzy import fuzz

def load_data(file_path):
    """Load data from a CSV or Excel file."""
    try:
        logging.info(f"Loading data from {file_path}")

        # Check the file extension
        _, file_extension = os.path.splitext(file_path)

        # Load data based on file extension
        if file_extension == '.csv':
            return pd.read_csv(file_path)
        elif file_extension in ['.xls', '.xlsx']:
            return pd.read_excel(file_path)
        else:
            logging.error("Unsupported file format")
            return None

    except FileNotFoundError:
        logging.error(f"The file {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        logging.error("The file is empty.")
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return None

def apply_fuzzy_aliases(df, alias_mapping, threshold=80):
    """Apply fuzzy matching to rename columns based on alias mapping."""
    df.columns = df.columns.str.lower()  # Convert column names to lowercase
    for standard_name, variants in alias_mapping.items():
        for col in df.columns:
            for variant in variants:
                # Rename columns if similarity exceeds threshold
                if fuzz.ratio(col, variant) >= threshold:
                    df.rename(columns={col: standard_name}, inplace=True)
    return df

def select_columns(df, desired_columns):
    """Select only the columns that exist in the DataFrame."""
    return df[[col for col in desired_columns if col in df.columns]]

def standardize_time_format(time_str):
    """Standardize time format."""
    # Adjust logic based on your specific time formats
    if '-' in time_str:
        return time_str.replace('-', ' to ')
    return time_str

def standardize_time_data(df):
    """Create new columns for standardized day/date and time."""
    df['Day/Date'] = df.apply(
        lambda row: f"{row['Weekday']} {row['Date']}" if 'Weekday' in row and 'Date' in row else row.get('Weekday') or row.get('Date'),
        axis=1
    )
    df['Time'] = df['Time'].apply(lambda x: standardize_time_format(x))
    return df

def preprocess_data(df, alias_mapping, desired_columns):
    """Preprocess the DataFrame by cleaning and selecting data."""
    try:
        logging.info("Preprocessing data")
        df.dropna(axis=1, how='all', inplace=True)  # Drop completely empty columns
        df = standardize_time_data(df)  # Standardize time data
        df = apply_fuzzy_aliases(df, alias_mapping)  # Apply fuzzy matching for column names
        df = select_columns(df, desired_columns)  # Select desired columns
        return df.astype(str)  # Convert all data to string type
    except Exception as e:
        logging.error(f"An error occurred during preprocessing: {e}")
        return None
