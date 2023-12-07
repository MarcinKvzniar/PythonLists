import argparse
import os
import sys
import shingle_utilities


def main():
    """
    Function that prints n most common shingles from
    a text provided in console and finished with EOF character or
    provided in a text file (.txt) in operating system shell.

    Raises:
        TypeError: If n or k are not integers
        ValueError: If n or k are not greater than 0
    """
    parser = argparse.ArgumentParser(
        prog="k-shingles printer",
        description="Prints the n most common k-shingles from text")

    parser.add_argument('-n', type=int, default=20,
                        help="The amount of k-shingles to print\n"
                             "Default value: 10")

    parser.add_argument('-k', type=int, default=2,
                        help="The length of each shingle\n"
                             "Default value: 2")

    parser.add_argument('-file', type=str, required=False,
                        help="Optional file provided by user, "
                             "to search for shingles in it.")

    args = parser.parse_args()

    if not isinstance(args.n, int):
        raise TypeError("n must be an integer")

    if not isinstance(args.k, int):
        raise TypeError("k must be an integer")

    if args.n <= 0:
        raise ValueError("n must be greater than 0")
    if args.k <= 0:
        raise ValueError("k must be greater than 0")

    if args.file:
        if not os.path.isfile(args.file):
            print(f"File {args.file} does not exist.")
            sys.exit(1)

        with open(args.file, 'r') as f:
            text = f.read()
    else:
        text = ""
        while True:
            try:
                line = input()
                text += line + "\n"
            except EOFError:
                break

    tokens = text.split()

    all_shingles = shingle_utilities.shingles(tokens, args.k)

    sorted_shingles = sorted(all_shingles.items(),
                             key=lambda item: item[1], reverse=True)

    for shingle, count in sorted_shingles[:args.n]:
        shingle_str = " - ".join(shingle)
        print(f"{shingle_str}: {count}")


if __name__ == '__main__':
    try:
        main()
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")


