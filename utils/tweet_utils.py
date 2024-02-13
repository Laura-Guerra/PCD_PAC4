"""
Module for text processing operations.

Functions:
    - normalize_tweet(tweet: dict) -> dict
    - clean_tweet(tweet: dict, words_list: list) -> dict
    - add_vocab(words: list, vocab: list) -> list
    - tweet_vocab(tweet: dict, vocab: set) -> tuple
    - add_frequencies_to_tweets(tweets, frequencies) -> list
"""

from utils.text_utils import count_words, delete_words, normalize_text
from utils.text_utils import remove_urls, split_string


def normalize_tweet(tweet: dict) -> dict:
    """
    Normalize the text of a tweet in the given dictionary.

    Args:
        tweet (dict): A dictionary representing a tweet.

    Returns:
        dict: The dictionary with the cleaned text.
    """
    cleaned_text = remove_urls(tweet['text'])
    cleaned_text = normalize_text(cleaned_text)
    tweet['text'] = cleaned_text

    return tweet


def clean_tweet(tweet: dict, words_list: list) -> dict:
    """
    Cleans the text of a tweet in the given dictionary.

    Args:
        tweet (dict): A dictionary representing a tweet.

    Returns:
        dict: The dictionary with the cleaned text.
    """
    cleaned_text = delete_words(tweet['text'], words_list)
    tweet['text'] = cleaned_text

    return tweet


def add_vocab(words: list, vocab: list) -> list:
    """
    Adds new words from a list to a vocabulary list.

    Args:
        words (list): A list of words to be added.
        vocab (list): The vocabulary list to update.

    Returns:
        list: The updated vocabulary list.
    """
    new_words = [word for word in words if word not in vocab]
    vocab.extend(new_words)
    return vocab


def tweet_vocab(tweet: dict, vocab: set) -> tuple:
    """_summary_
    Calculates the word count of a tweet and updates the vocabulary.

    Args:
        tweet (dict): A dictionary representing a tweet.
        vocab (set): The vocabulary set to update.

    Returns:
        tuple: A tuple containing the word count dictionary and the updated
        vocabulary set.
    """
    words = split_string(tweet['text'])
    tweet_count = count_words(words)
    vocab.update(words)
    return tweet_count, vocab


def add_frequencies_to_tweets(tweets: list,
                              frequencies: list, freq_col: str) -> list:
    """
    Adds a 'words' key to each tweet dictionary, with the corresponding
    frequencies.

    Args:
        tweets (list): A list of tweet dictionaries.
        frequencies (list): A list of frequency dictionaries.

    Returns:
        list: The modified list of tweet dictionaries.
    """
    for tweet, freq in zip(tweets, frequencies):
        tweet[freq_col] = freq
    return tweets
