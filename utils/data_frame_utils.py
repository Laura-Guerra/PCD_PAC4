"""
Utility functions for DataFrame operations.

Functions:
    - get_unique_clusters(df: pd.DataFrame, column: str) -> list
    - calculate_missing_pct(df: pd.DataFrame, column: str) -> float
    - drop_na(df: pd.DataFrame, column: str) -> None:
    - df_column_to_dict(df: pd.DataFrame, column: str) -> pd.DataFrame
"""

import ast
import pandas as pd


def get_unique_clusters(df: pd.DataFrame, column: str) -> list:
    """
    Get the unique clusters based on a column in a DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to extract the unique clusters
            from.
        column (str): The column name to consider for creating clusters.

    Returns:
        list: A list of unique clusters based on the specified column.
    """
    clusters = df[column].unique().tolist()
    return clusters


def calculate_missing_pct(df: pd.DataFrame, column: str) -> float:
    """
    Calculate the percentage of missing values in a column of a DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to calculate the missing
            percentage from.
        column (str): The column name to calculate the missing percentage.

    Returns:
        float: The percentage of missing values in the specified column.
    """
    rows_count = df.shape[0]
    missing_count = df[column].isna().sum()
    missing_percentage = (missing_count / rows_count) * 100
    return missing_percentage


def drop_na(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Drop rows with missing values in the specified column of a DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to drop rows from.
        column (str): The column name to check for missing values.

    Returns:
        df (pd.DataFrame): The DataFrame without nan.
    """
    percentage = calculate_missing_pct(df, column)
    if percentage == 0:
        print(f"There are no missing values in {column} column")
    else:
        print(f"{column} column has {percentage:.2f}% missing values.")
        df.dropna(subset=[column], inplace=True)
    return df


def df_column_to_dict(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Convert a dictionary column in a pandas DataFrame from string to
    dictionary.

    Args:
        df (pd.DataFrame): The DataFrame containing the dictionary
            column.
        column (str): The name of the dictionary column to convert.

    Returns:
        pd.DataFrame: The DataFrame with the converted dictionary column.
    """
    df[column] = df[column].apply(ast.literal_eval)
    return df
