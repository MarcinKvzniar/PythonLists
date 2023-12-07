"""
Module containing methods used either in shingle.py and compare.py
"""


def shingles(t, k):
    """
    Creates a multiset(dictionary) of k-shingles from a list of tokens t

    In this code, a dictionary is used as a multiset (or bag) data
    structure. A multiset is a generalization of the concept of a set
    that, unlike a set, allows multiple instances of the multiset's
    elements. The dictionary keys represent the unique elements found
    in the multiset, while the corresponding dictionary values count
    the number of occurrences of each element.

    Arguments:
        t (list): list of strings
        k (int): the length of each single

    Returns:
        all_singles (dictionary): A dictionary containing shingle as
            a key value and number of their occurrences as an item.

    Raises:
        ValueError: if k is not greater than 0
        TypeError: If k (length of each single) is not an integer.
                   If t is not a list.
                   If any of elements in list t is not a string
    """
    if not isinstance(k, int):
        raise TypeError("k must be an integer.")

    if k <= 0:
        raise ValueError("k must be greater than 0.")

    if not isinstance(t, list) or not all(isinstance(x, str) for x in t):
        raise TypeError("t must be a list of strings")

    all_shingles = {}

    for i in range(len(t) - k + 1):
        k_shingle = tuple(t[i: i + k])

        if k_shingle in all_shingles:
            all_shingles[k_shingle] += 1
        else:
            all_shingles[k_shingle] = 1

    return all_shingles


if __name__ == '__main__':
    try:
        t = ["one", "two", "three", "four", "five", "one", "two"]
        k = 2
        all_singles = shingles(t, k)
        print(all_singles)
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")
