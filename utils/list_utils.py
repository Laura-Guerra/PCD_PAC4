"""
Module for list processing functions.

Functions:
    - apply_function_to_list(func, lst, **kwargs) -> list
    - print_list(lst: list, n: int = 5) -> None
"""


def apply_function_to_list(func, lst, **kwargs) -> list:
    """
    Applies a function to each element of a list and returns the results in a
    new list.

    Args:
        func (function): The function to apply to each element of the list.
        lst (list): The list of elements to process.
        **kwargs: Additional keyword arguments to be passed to the function.

    Returns:
        list: A new list with the results of applying the function to each
        element.
    """
    return [func(item, **kwargs) for item in lst]


def print_list(lst: list, n: int = 5) -> None:
    """
    Prints the first or last 'n' elements of the provided list on a separate
    line.

    Args:
        lst (list): List from which elements will be printed.
        n (int, optional): Number of elements to print. If positive,
            the first 'n' elements will be printed. If negative,
            the last 'n' elements will be printed. Default is 5.
    """
    if n > 0:
        elements = lst[:n]
    else:
        elements = lst[n:]

    for element in elements:
        print(element)

    print()
