"""
Module for word cloud generation and visualization.

Functions:
    - set_word_clouds_and_frequency_dicts(df, clusters, cluster_col, freq_col)
        -> Tuple[dict, dict]
    - show_word_clouds(word_clouds)
    - get_most_common_words(freq_dicts, words_num=25) -> dict
    - plot_word_frequencies(words_freq, cluster_name)
"""

from collections import Counter
from typing import Tuple
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
from utils import file_utils as fu
from utils import constants as ct


def set_word_clouds_and_frequency_dicts(
    df: pd.DataFrame, clusters: list, cluster_col: str, freq_col: str
) -> Tuple[dict, dict]:
    """
    Generate word clouds and frequency dictionaries for each cluster.

    Args:
        df (pd.DataFrame): The DataFrame with the data.
        clusters (list): The list of unique clusters.
        cluster_col (str): The column with the clusters.
        freq_col (str): The column with the frequency dictionaries.

    Returns:
        Tuple(Dict, Dict): A tuple with two dictionaries: one with clusters as
            keys and WordCloud objects as values, the other one with clusters
            as keys and frequency dictionaries as values.
    """
    word_clouds = {}
    freq_dicts = {}

    for cluster in clusters:
        df_cluster = df[df[cluster_col] == cluster]
        combined_freqs = Counter()

        for freqs in df_cluster[freq_col]:
            combined_freqs.update(freqs)

        freq_dicts[cluster] = combined_freqs

        word_cloud = WordCloud(
            width=800, height=400, max_words=200, background_color="white"
        ).generate_from_frequencies(combined_freqs)

        word_clouds[cluster] = word_cloud

    return word_clouds, freq_dicts


def show_word_clouds(word_clouds: dict) -> None:
    """
    Display word clouds for each cluster.

    Args:
        word_clouds (dict): A dictionary with clusters as keys and WordCloud
            objects as values.

    Returns:
        None
    """
    for cluster, word_cloud in word_clouds.items():
        plt.imshow(word_cloud, interpolation="bilinear")
        plt.axis("off")

        fig_name = "word_cloud_cluster" + str(cluster)
        fig_path = fu.set_file_path(ct.FIGS_PATH, fig_name)
        plt.savefig(fig_path, bbox_inches='tight', pad_inches=0)
        print(f"Cluster {cluster} word cloud saved in figures folder")


def get_most_common_words(freq_dicts, words_num=25) -> dict:
    """
    Get the most common words and their frequencies for each cluster.

    Args:
        freq_dicts (dict): A dictionary with clusters as keys and frequency
            dictionaries as values.
        words_num (int, optional): The number of words to display. Default is
            25.

    Returns:
        dict: A dictionary with clusters as keys and dictionaries of the most
            common words and their frequencies as values.
    """
    most_common_words = {}
    for cluster_key, freq_dict in freq_dicts.items():
        sorted_items = sorted(freq_dict.items(),
                              key=lambda item: item[1], reverse=True)
        top_items = sorted_items[:words_num]
        most_common_words[cluster_key] = dict(top_items)

    return most_common_words


def plot_word_frequencies(words_freq, cluster_name) -> None:
    """
    Generate histograms for each cluster.

    Args:
        words_freq (dict): A dictionary with clusters as keys and dictionaries
            of the most common words and their frequencies as values.
        cluster_name (str): The name of the cluster column.

    Returns:
        None
    """
    for cluster, word_freqs in words_freq.items():
        words = list(word_freqs.keys())
        frequencies = list(word_freqs.values())

        plt.figure(figsize=(10, 5))
        plt.bar(words, frequencies, color="blue", width=0.4)

        plt.xlabel("Words")
        plt.ylabel("Frequency")
        plt.title(f"Word Frequency Histogram for {cluster_name} = {cluster}")
        plt.xticks(rotation=45)

        fig_name = "histogram_cluster" + str(cluster)
        fig_path = fu.set_file_path(ct.FIGS_PATH, fig_name)
        plt.savefig(fig_path)
        print(f"Cluster {cluster} histogram saved in figures folder")
