import pytest
from utils import tweet_utils as tp

class TestTweetProcessing:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.tweet1 = {
            "text": "Mars is cool! #Martian www.mars.com", "user": "aliens"}
        self.tweet2 = {
            "text": "Mars Mars #Martian www.mars.com", "user": "aliens"}
        self.tweet3 = {
            "text": "Mars is cool #Martian www.mars.com like",
            "user": "aliens cool"}
        self.tweets = [
            {"text": "Mars is cool! #Martian www.mars.com",
                "user": "Laura", "age": 17},
            {"text": "Mars has aliens.", "user": "Yasmin", "age": 18},
            {"text": "I don't like mars :( mars mars mars",
             "user": "Lidia", "age": 15}
        ]
        self.word_list = ["cool", "like"]

    def test_normalize_tweet(self):
        assert tp.normalize_tweet(self.tweet1) == {
            "text": "mars is cool martian ", 'user': 'aliens'}

    def test_clean_tweet(self):
        assert tp.clean_tweet(self.tweet1, self.word_list) == {
            "text": "Mars is cool! #Martian www.mars.com", "user": "aliens"}
        assert tp.clean_tweet(self.tweet3, self.word_list) == {
            "text": "Mars is #Martian www.mars.com", "user": "aliens cool"}

    def test_add_vocab(self):
        assert tp.add_vocab(["Mars", "Venus"], self.word_list) == [
            'cool', 'like', 'Mars', 'Venus']

    def test_tweet_vocab(self):
        word_count, vocab = tp.tweet_vocab(self.tweet2, set(self.word_list))
        assert word_count == {
            '#Martian': 1, 'Mars': 2, 'www.mars.com': 1}
        assert vocab == set(["#Martian", "Mars",
                             "www.mars.com", "like", "cool"])

    def test_add_frequencies_to_tweets(self):
        freqs = [
            {"mars": 1, "is": 1, "cool": 1, "martian": 1, "www": 1, "com": 1},
            {"mars": 1, "has": 1, "aliens": 1},
            {"i": 1, "don": 1, "t": 1, "like": 1, "mars": 4}
        ]
        tp.add_frequencies_to_tweets(self.tweets, freqs, 'words')
        assert self.tweets == [
            {
                "text": "Mars is cool! #Martian www.mars.com",
                "user": "Laura",
                "age": 17,
                "words": {"mars": 1, "is": 1, "cool": 1, "martian": 1,
                          "www": 1, "com": 1}
            },
            {
                "text": "Mars has aliens.",
                "user": "Yasmin", "age": 18,
                "words": {"mars": 1, "has": 1, "aliens": 1}
            },
            {
                "text": "I don't like mars :( mars mars mars",
                "user": "Lidia",
                "age": 15,
                "words": {"i": 1, "don": 1, "t": 1, "like": 1, "mars": 4}
            }
        ]
