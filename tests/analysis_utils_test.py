import pandas as pd
import pytest
from collections import Counter
from utils.analysis_utils import set_word_clouds_and_frequency_dicts
from utils.analysis_utils import get_most_common_words


class TestAnalysisUtils:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.df = pd.DataFrame(
            {
                "clusters": ["c1", "c1", "c2", "c2"],
                "freqs": [
                    {"word1": 5, "word2": 3},
                    {"word1": 2, "word2": 2, "word3": 1},
                    {"word1": 3, "word3": 4},
                    {"word2": 1, "word3": 1, "word4": 5},
                ],
            }
        )
        self.clusters = ["c1", "c2"]

    def test_frequency_dicts_of_set_word_clouds_and_frequency_dicts(self):
        wordclouds, freq_dicts = set_word_clouds_and_frequency_dicts(
            self.df, self.clusters, "clusters", "freqs"
        )

        assert set(wordclouds.keys()) == set(self.clusters)

        assert freq_dicts["c1"] == Counter({"word1": 7, "word2": 5, "word3": 1})
        assert freq_dicts["c2"] == Counter({"word1": 3, "word3": 5,
                                            "word2": 1, "word4": 5})

    def test_get_most_common_words_waith_freqs_of_dict_of_dict(self):
        freq_dicts = {
            "c1": Counter({"word1": 7, "word2": 5, "word3": 1}),
            "c2": Counter({"word1": 3, "word3": 5, "word2": 1, "word4": 5}),
        }
        most_common = get_most_common_words(freq_dicts, 2)

        assert most_common["c1"] == {"word1": 7, "word2": 5}
        assert most_common["c2"] == {"word3": 5, "word4": 5}
