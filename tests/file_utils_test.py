import csv
import os
import shutil
import pandas as pd
import pytest
from utils.file_utils import unzip_file, read_csv_to_dict_list
from utils.file_utils import dict_list_to_csv, csv_to_df, set_file_path


class TestFileUtils:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.zip_path = 'tests/test_files/test.zip'
        self.output_path = 'tests/test_files'
        self.csv_path = 'tests/test_files/test.csv'
        self.dataset = [
            {
                "sentiment": "0",
                "id": "1",
                "date": "2023-06-01",
                "query": "NO_QUERY",
                "user": "user1",
                "text": "I'm feeling great today!"
            },
            {
                "sentiment": "1",
                "id": "2",
                "date": "2023-06-02",
                "query": "NO_QUERY",
                "user": "user2",
                "text": "This is an amazing day!"
            },
            {
                "sentiment": "0",
                "id": "3",
                "date": "2023-06-03",
                "query": "NO_QUERY",
                "user": "user3",
                "text": "Feeling a little tired."
            }
        ]
        self.base_dir = 'base'
        self.file_name = 'file.txt'

    def test_unzip_file(self):
        unzip_file(self.zip_path, self.output_path)
        assert os.path.exists(self.output_path)

    def test_convert_csv_to_dict_list(self):
        data = read_csv_to_dict_list(self.csv_path)
        assert data == self.dataset

    def test_convert_dict_list_to_csv(self):
        dict_list_to_csv(self.csv_path, self.dataset)
        with open(self.csv_path, 'r', encoding="utf8") as f:
            reader = csv.DictReader(f)
            for row, expected in zip(reader, self.dataset):
                assert row == expected

    def test_csv_to_df(self):
        df = csv_to_df(self.csv_path)
        assert isinstance(df, pd.DataFrame)

    def test_set_file_path(self):
        expected_path = os.path.join(self.base_dir, self.file_name)
        file_path = set_file_path(self.base_dir, self.file_name)
        assert file_path == expected_path
        assert os.path.isdir(self.base_dir)
    
    @classmethod
    def teardown_class(cls):
        if os.path.exists('base'):
            shutil.rmtree('base')
