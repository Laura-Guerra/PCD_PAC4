"""
Main program file for PAC 4 of "Programació per a la ciencia de dades" course
at UOC.

Author: Laura Guerra
Date: June 2023
"""

from utils import analysis_utils as au
from utils import constants as ct
from utils import data_frame_utils as dfu
from utils import file_utils as fu
from utils import list_utils as lu
from utils import tweet_utils as tu


def execute_pac4():
    """
    Main function for the execution of the PAC 4 of "Programació per a la
    ciencia de dades" course. It performs the execution of all the exercises of
    the PAC.
    """

    # Exercise 1.2
    tweets = exercise_1()

    # Exercise 2
    tweets = exercise_2(tweets)

    # Exercise 3
    # vocabulary is not used, but it is required by the exercise statement.
    freq_list, vocabulary = exercise_3(tweets)

    # Exercise 4
    exercise_4(tweets, freq_list)

    # Exercise 5
    freq_dicts = exercise_5()

    # Exercise 6
    exercise_6(freq_dicts)

    # Exercise 7 in report.pdf
    print("Exercise 7: Answer in report.pdf")

def exercise_1():
    """
    Execute the exercise 1
    Unzips the zipped data file for the PAC and reads a csv file and returns it
    as a list of dictionaries
    Returns:
        list: A list of dictionaries representing the tweets data.
    """
    # Exercise 1.1
    zip_file_path = fu.set_file_path(ct.DATA_FOLDER, ct.TWITTER_REDUCED_ZIP)
    fu.unzip_file(zip_file_path, ct.DATA_FOLDER)

    # Exercise 1.2
    csv_data_path = fu.set_file_path(ct.DATA_FOLDER, ct.TWITTER_REDUCED_CSV)
    tweets_list = fu.read_csv_to_dict_list(csv_data_path)
    print("Exercise 1.2")
    lu.print_list(tweets_list)
    return tweets_list


def exercise_2(tweets_list):
    """
    Execute the exercise 2
    Applies normalization and cleaning to the tweets data.
    Args:
        tweets_list (list): The list of tweets data.
    Returns:
        list: The cleaned and normalized tweets data.
    """
    # Exercise 2.1
    tweets = lu.apply_function_to_list(tu.normalize_tweet, tweets_list)

    # Exercise 2.2
    tweets = lu.apply_function_to_list(tu.clean_tweet, tweets_list,
                                       words_list=ct.STOP_WORDS)
    print("Exercise 2")
    lu.print_list(tweets, -5)
    return tweets


def exercise_3(tweets):
    """
    Execute the exercise 3
    Generates the vocabulary and frequency list from the tweets data.
    Args:
        tweets (list): The cleaned and normalized tweets data.
    Returns:
        list, list: The frequency list and vocabulary list of the tweets data.
    """
    vocab = set()
    results = lu.apply_function_to_list(tu.tweet_vocab, tweets, vocab=vocab)
    freq_list = [result[0] for result in results]
    vocab = sorted(list(vocab))

    print("Exercise 3")

    print("Word's count of the first 5 tweets")
    lu.print_list(freq_list, 5)
    print("First 10 words of tweets vocabulary")
    lu.print_list(vocab, 10)

    return freq_list, vocab


def exercise_4(tweets, freq_list):
    """
    Execute the exercise 4
    Adds frequency data to the tweets, prints the 20th processed tweet,
    and writes the processed tweets data to a csv file.
    Args:
        tweets (list): The cleaned and normalized tweets data.
        freq_list (list): The frequency list of the tweets data.
    Returns:
        None
    """
    print("Exercise 4")
    print("Element 20 of the processed dataset")
    processed_tweets = tu.add_frequencies_to_tweets(tweets,
                                                    freq_list, ct.FREQ_COLUMN)
    print(processed_tweets[20])

    processed_file_path = fu.set_file_path(ct.DATA_FOLDER, ct.PROCESSED_FILE)
    fu.dict_list_to_csv(processed_file_path, processed_tweets)


def exercise_5():
    """
    Execute the exercise 5
    Performs several operations to create clusters, drop NA values, and 
    generate wordclouds and frequency dictionaries.
    Returns:
        clusters, freq_dicts: The clusters and frequency dictionaries of the
        tweets data.
    """
    processed_file_path = fu.set_file_path(ct.DATA_FOLDER, ct.PROCESSED_FILE)
    tweets_df = fu.csv_to_df(processed_file_path)
    tweets_df = dfu.df_column_to_dict(tweets_df, ct.FREQ_COLUMN)

    print("Exercise 5.1")
    clusters = dfu.get_unique_clusters(tweets_df, ct.CLUSTERS_COLUMN)
    print(f"There are {len(clusters)} clusters \n")

    print("Exercise 5.2")
    tweets_df = dfu.drop_na(tweets_df, 'text')
    print()

    print("Exercise 5.3")
    result = au.set_word_clouds_and_frequency_dicts(tweets_df, clusters,
                                                    ct.CLUSTERS_COLUMN,
                                                    ct.FREQ_COLUMN)
    (wordclouds, freq_dicts) = result
    au.show_word_clouds(wordclouds)
    print()

    return freq_dicts


def exercise_6(freq_dicts):
    """
    Execute the exercise 6
    Gets the most common words and plots their frequencies.
    Args:
        freq_dicts (dict): The frequency dictionaries of the tweets data.
    """
    print("Exercise 6")
    common_words = au.get_most_common_words(freq_dicts)
    au.plot_word_frequencies(common_words, ct.CLUSTERS_COLUMN)
    print()


if __name__ == "__main__":
    execute_pac4()
