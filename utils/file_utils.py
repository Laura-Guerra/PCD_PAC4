"""
Module for file handling operations.

Functions:
    - unzip_file(zip_path: str, output_path: str) -> None
    - read_csv_to_dict_list(file_path: str) -> list
    - dict_list_to_csv(out_path: str, dataset: list)
    - csv_to_df(file_path: str) -> pd.DataFrame
    - set_file_path(base_dir: str, file_name: str) -> str
"""
import zipfile
import csv
import os
import pandas as pd


def unzip_file(zip_path: str, output_path: str) -> None:
    """
    Unzips a file to the specified output path.

    Args:
        zip_path (str): The path of the zip file.
        output_path (str): The output path where the zip file will be extracted
    """

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(output_path)


def read_csv_to_dict_list(file_path: str) -> list:
    """
    Reads a CSV file and returns its contents as a list of dictionaries.

    Args:
        file_path (str): The path of the CSV file.

    Returns:
        list[dict]: A list of dictionaries representing the rows of the CSV
            file
    """

    with open(file_path, "r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        data = list(reader)
    return data


def dict_list_to_csv(out_path: str, dataset: list):
    """
    Writes a list of dictionaries to a CSV file.

    Args:
        out_path (str): The output file path.
        dataset (list): A list of dictionaries representing the data.
    """

    fieldnames = dataset[0].keys()
    with open(out_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(dataset)


def csv_to_df(file_path: str) -> pd.DataFrame:
    """
    Converts a CSV file to a DataFrame.

    Args:
        file_path (str): Path of the CSV file.

    Returns:
        pd.DataFrame: DataFrame generated from the CSV file.

    Raises:
        FileNotFoundError: If the CSV file does not exist.
        Exception: If an error occurs while reading the CSV file.
    """

    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError as e:
        raise FileNotFoundError("The CSV file does not exist.") from e


def set_file_path(base_dir: str, file_name: str) -> str:
    """
    Create the complete file path by concatenating the base directory and file
    name.

    Args:
        base_dir (str): The base directory where the file is located.
        file_name (str): The name of the file.

    Returns:
        str: The complete file path.

    Raises:
        OSError: If the base directory cannot be created.
    """

    if not os.path.exists(base_dir):
        try:
            os.makedirs(base_dir)
        except OSError as e:
            raise OSError(f"Failed to create {base_dir} directory") from e
    return os.path.join(base_dir, file_name)
