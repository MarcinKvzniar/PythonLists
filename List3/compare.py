import argparse
import os
import string
import sys

import shingle_utilities


def jaccard_similarity(set1, set2):
    """
    This function calculates a jaccard similarity (index) for two
    multi-sets of shingles. Jaccard similarity is defined as the size
    of the intersection divided by the size of the union of the sets.

    Arguments:
        set1, set2 (dict): Dictionaries containing shingle as a key and
            number of its occurrences as an item.

    Returns:
        jaccard_index (float): The Jaccard index of provided sets

    Raises:
        ValueError:
            - If one of the sets is empty
            - If value of union is equal to 0
             (to avoid ZeroDivisionError)
        TypeError:
            - If set1 or set2 are not dictionaries
    """
    if not isinstance(set1, dict) or not isinstance(set2, dict):
        raise TypeError("Both sets must be dictionaries.")

    if not set1 or not set2:
        raise ValueError("One of the sets is empty.")

    intersection, union = 0, 0

    for key in set1:
        if key in set2:
            intersection += min(set1[key], set2[key])
        union += set1[key]

    for key in set2:
        union += set2[key]

    union -= intersection

    if union == 0:
        raise ValueError("Union of sets is 0."
                         " Cannot calculate Jaccard Similarity.")

    jaccard_index = intersection / union

    return jaccard_index


def main():
    """
    Function containing a code that prints the Jaccard Similarity of
    two sets of shingles. Sets are determined using function shingles
    from shingle_utilities.py module and are taken from two files
    that user is required to enter in operating system shell.
    Additionally, arg parser contains an argument that if enabled
    removes punctuation marks from the provided text files.

    Raises:
        ValueError: In case when function shingles or jaccard_similarity
            raises it.
        TypeError: In case when function shingles or jaccard_similarity
            raises it.
    """
    parser = argparse.ArgumentParser(
        prog="Text comparator",
        description="Compares two text files in terms of Jaccard similarity.")

    parser.add_argument('--query', type=str, required=True,
                        help="Path to the first text file.")

    parser.add_argument('--target', type=str, required=True,
                        help="Path to the second text file.")

    parser.add_argument('-k', type=int, default=2,
                        help="The length of each shingle\n"
                             "Default value: 2")

    parser.add_argument('--remove_punctuation', action='store_true',
                        help="Removes punctuation marks from the text.")

    args = parser.parse_args()

    if not os.path.isfile(args.query):
        print(f"File {args.query} does not exist.")
        sys.exit(1)

    if not os.path.isfile(args.target):
        print(f"File {args.target} does not exist.")
        sys.exit(1)

    with open(args.query, 'r') as f:
        query_text = f.read()

    with open(args.target, 'r') as f:
        target_text = f.read()

    if args.remove_punctuation:
        query_text = query_text.translate(
            str.maketrans('', '', string.punctuation))
        target_text = target_text.translate(
            str.maketrans('', '', string.punctuation))

    query_tokens = query_text.split()
    target_tokens = target_text.split()

    query_shingles = shingle_utilities.shingles(query_tokens, args.k)
    target_shingles = shingle_utilities.shingles(target_tokens, args.k)

    try:
        jaccard_index = jaccard_similarity(query_shingles, target_shingles)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except TypeError as e:
        print(f"Error: {e}")
        sys.exit(1)

    print(f"The Jaccard Similarity between the two provided"
          f" text files is: {jaccard_index} ")


if __name__ == '__main__':
    try:
        main()
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")


