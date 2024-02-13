"""
Module for text processing operations.

Functions:
    - normalize_text(text: str) -> str
    - remove_urls(text: str) -> str
    - delete_words(text: str, words_list: list) -> str
    - count_words(words: list) -> dict
    - split_string(text: str) -> list
"""


import re
from collections import Counter


def normalize_text(text: str) -> str:
    """
    Cleans the given text by converting to lowercase and removing special
    characters.

    Args:
        text (str): The text to be cleaned.

    Returns:
        str: The cleaned text.
    """
    cleaned_text = text.lower()
    cleaned_text = re.sub(r'[^a-z0-9 ]', '', cleaned_text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)

    return cleaned_text


def remove_urls(text: str) -> str:
    """
    Removes URLs from the given text.

    Args:
        text (str): The text to remove URLs from.

    Returns:
        str: The text with URLs removed.
    """
    url_pattern = (
        r'((https?:\/\/)|(www\.))' +
        r'[-a-z0-9@:%._\+~#=]{1,256}' +
        r'\.[a-z0-9()]{1,6}' +
        r'\b([-a-z0-9()@:%_\+.~#?&//=]*)'
    )
    cleaned_text = re.sub(url_pattern, '', text, flags=re.IGNORECASE)

    return cleaned_text


def delete_words(text: str, words_list: list) -> str:
    """
    Deletes specified words from the given text.

    Args:
        words_to_delete (list): A list of words to be deleted.
        text (str): The text to modify.

    Returns:
        str: The modified text with specified words deleted.
    """
    cleaned_text = ' '.join(word for word in text.split() if
                            word not in words_list)
    return cleaned_text


def count_words(words: list) -> dict:
    """
    Calculates the frequency of each word in the given list.

    Args:
        words (list): The list to analyze.

    Returns:
        dict: A dictionary containing the word frequencies.
    """
    word_count = dict(Counter(words))

    return word_count


def split_string(text: str) -> list:
    """
    Splits a string into a list of words.

    Args:
        text (str): The string to split.

    Returns:
        list: A list of words.
    """
    return text.split()
