import pandas as pd
import pytest
from utils.data_frame_utils import get_unique_clusters, calculate_missing_pct
from utils.data_frame_utils import drop_na, df_column_to_dict


class TestDataFrameUtils:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.df = pd.DataFrame({
            'clusters': ['c1', 'c1', 'c2', 'c2', None],
            'values': [1, 2, 3, None, 5],
            'dicts': ["{'a': 1, 'b': 3}", "{'b': 2}", "{'c': 3}", "{'d': 4}",
                      "{'e': 5}"]
        })

    def test_get_unique_values_of_column_df(self):
        clusters = get_unique_clusters(self.df, 'clusters')
        assert clusters == ['c1', 'c2', None]

    def test_calculate_pct_of_missing_val_of_column(self):
        missing_pct = calculate_missing_pct(self.df, 'values')
        assert missing_pct == 20.0

    def test_drop_na_of_a_column(self):
        df_no_na = drop_na(self.df, 'clusters')
        assert len(df_no_na) == 4

    def test_convert_df_column_to_dict(self):
        df_dict = df_column_to_dict(self.df, 'dicts')
        assert df_dict.loc[0, 'dicts'] == {'a': 1, 'b': 3}
