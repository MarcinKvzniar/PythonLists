import random
import matplotlib.pyplot as plt
import numbers

def get_valid_float_input(insert):
    """
    This auxiliary function is used to constantly ask user for an input until they will provide
    a valid floating-point number input

    Arguments:
        insert (str): string input that we want to check if is a floating-number

    Returns:
        Provided input converted to a floating-point number

    Raises:
        ValueError: if a provided number is not a valid floating-point number

    """
    while True:
        try:
            return float(input(insert))
        except ValueError:
            print("Error: Invalid input, please enter a valid floating-point number.")


def get_valid_int_input(insert):
    """
        This auxiliary function is used to constantly ask user for an input until they will provide
        a valid integer number input

        Arguments:
            insert (str): string input that we want to check if is an integer

        Returns:
            Provided input converted to an integer number

        Raises:
            ValueError: if a provided number is not a valid integer

        """
    while True:
        try:
            return int(input(insert))
        except ValueError:
            print("Error: Invalid input, please enter a valid integer number.")


def weekday(day, month, year):
    """
    This function calculates the particular day of the week
    represented by integers from 0 to 6 for a given date.

    Arguments:
        day (int): The day of the month, ranging from 1 to 31.
        month (int): The month of the year, ranging from 1 to 12.
        year (int): The year, which should be a positive integer.

    Returns:
        d0: an integer from 0 to 6, representing the day of the week,
            where 0 means Sunday, 1 means Monday and so on.

    Raises:
        ValueError: If the provided day, month, or year
                    is not within the valid range.
    """

    if day not in range(1, 32) or not isinstance(day, int):
        raise ValueError("Day must be an integer between 1 and 31.")
    if month not in range(1, 13) or not isinstance(month, int):
        raise ValueError("Month must be an integer between 1 and 12.")
    if not year > 0 or not isinstance(year, int):
        raise ValueError("Year must be a bigger than 0 integer.")

    y0 = int(year - (14 - month) // 12)
    x = int(y0 + y0 // 4 - y0 // 100 + y0 // 400)
    m0 = int(month + 12 * ((14 - month) // 12) - 2)
    d0 = int((day + x + (31 * m0) // 12) % 7)

    return d0


def segment_length(Ap, Ak, Bp, Bk):
    """
    This function determines the range of intersection of two segments.
    Intersection of two segments is defined as the interval starting
    from the greatest of the starting points of segment A and segment B,
    and ending at the smallest of the ending points of these segments.

    Arguments:
        Ap (numeric): Starting point of segment A.
        Ak (numeric): Ending point of segment A.
        Bp (numeric): Starting point of segment B.
        Bk (numeric): Ending point of segment B.

    Returns:
        tuple or None: A tuple containing the starting and ending
                       points of the intersection,
                       or None if there is no intersection.

    Raises:
        ValueError: If the input values are not valid numerals.
    """
    if (not isinstance(Ak, numbers.Number)
            or not isinstance(Ap, numbers.Number)
            or not isinstance(Bp, numbers.Number)
            or not isinstance(Bk, numbers.Number)):
        raise ValueError("Provided number must be a numeral type")

    start_intersection = max(Ap, Bp)
    end_intersection = min(Ak, Bk)

    if Bp > Ak or Ap > Bk:
        return None
    else:
        return start_intersection, end_intersection


def random_walk(n):
    """
    This function simulates a random 2D walk within the limits
    specified by the parameter n. The walker moves randomly
    in the horizontal and vertical directions within the range
    of -100 to 100 on both axes until the distance limit is reached.

    Arguments:
        n (int): Limit of maximum distance from the central point (0, 0).

    Returns:
        coordinates: List of tuples of current coordinates
                     of the walker in every iteration.

    Raises:
        ValueError: If the provided limit n
                    is not a bigger than 0 integer.
    """
    if n < 0 or not isinstance(n, int):
        raise ValueError("n has to be a bigger than 0 integer")

    pos_x = 0
    pos_y = 0
    horizontal_move = random.choice([-1, 1])
    vertical_move = random.choice([-1, 1])
    coordinates = [(pos_x, pos_y)]

    while -100 < pos_x < 100 and -100 < pos_y < 100:
        if random.choice([True, False]):
            pos_x += horizontal_move
        else:
            pos_y += vertical_move

        coordinates.append((pos_x, pos_y))

    return coordinates


def dec2bin(dec):
    """
        This function converts a decimal number into
        its binary representation. It utilizes the algorithm of division
        by 2 and extraction of remainders.
        The idea of the representation of a negative binary number
        was taken from here:
        https://cs.calvin.edu/activities/books/rit/chapter5/negative.htm
        First number indicates a sign of provided number:
        0 in front of a binary number stands for a positive number
        1 in front of a binary number stands for a negative number

        Arguments:
            dec (int): A decimal number that user wants to
                 convert into binary.

        Returns:
            bin_str: A String type that holds
                     a binary representation of dec.

        Raises:
            ValueError: If the provided number is not an integer
        """
    if not isinstance(dec, int):
        raise ValueError("Provided number has to be an integer")

    pos_dec = abs(dec)
    bin_str = ""

    while pos_dec > 0:
        rem = pos_dec % 2
        pos_dec = pos_dec // 2
        bin_str = str(rem) + bin_str

    if dec > 0:
        bin_str = "0 " + bin_str
    elif dec == 0:
        bin_str = '0'
    else:
        bin_str = "1 " + bin_str

    return bin_str


def dna_complement(orig_strand):
    """
        This function takes an original DNA strand as input and
        generates the complementary strand

        Arguments:
            orig_strand (str): String type value that represents our
                               original DNA strand, consisting of the
                               characters 'A', 'C', 'T', 'G'.

        Returns:
            strand: A String type value that represents
                    complementary strand.

        Raises:
            ValueError: If the provided strand contains invalid chars.
    """
    strand = ""
    valid_bases = set('ACGT')

    for base in orig_strand:
        if base not in valid_bases:
            raise ValueError("Invalid DNA base provided.")

        if base == 'A':
            strand += 'T'

        elif base == 'T':
            strand += 'A'

        elif base == 'C':
            strand += 'G'

        elif base == 'G':
            strand += 'C'

    return strand


print("---------------Exercise1---------------")

days = ["Sunday", "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday"]

while True:
    try:
        day = get_valid_int_input("Enter the number of a day: ")
        if not 1 <= day <= 31:
            raise ValueError("Day must be between 1 and 31.")
        break
    except ValueError as e:
        print(f"Error: {e}")

while True:
    try:
        month = get_valid_int_input("Enter the number of a month: ")
        if not 1 <= month <= 12:
            raise ValueError("Month must be between 1 and 12.")
        break
    except ValueError as e:
        print(f"Error: {e}")

while True:
    try:
        year = get_valid_int_input("Enter the number of a year: ")
        if not year > 0:
            raise ValueError("Year must be bigger than 0.")
        break
    except ValueError as e:
        print(f"Error: {e}")

try:
    print(f"That day was a: {days[weekday(day, month, year)]}")
except ValueError as e:
    print(f"Error: {e}")

print("\n---------------Exercise2---------------")

Ap = get_valid_float_input("Enter a starting point of A segment: ")

Ak = get_valid_float_input("Enter an ending point of A segment: ")

Bp = get_valid_float_input("Enter a starting point of B segment: ")

Bk = get_valid_float_input("Enter a starting point of B segment: ")

print(f"Intersection segment: {segment_length(Ap, Ak, Bp, Bk)}")

print("\n---------------Exercise3---------------")

while True:
    try:
        n = get_valid_int_input("Enter the number of steps: ")
        coordinates = random_walk(n)
        x, y = zip(*coordinates)
        plt.plot(x, y, marker='o', linestyle='-', markersize=2)
        plt.xlabel('X Coordinate')
        plt.ylabel('Y Coordinate')
        plt.title('Walker\'s Trajectory')
        plt.grid(True)
        plt.show()
        break

    except ValueError as e:
        print(f"Error: {e}")

print("\n---------------Exercise4---------------")

dec = get_valid_int_input("Enter a number that you want to"
                          " display in binary system: ")
binary = dec2bin(dec)
print(f"Binary representation of {dec} is {binary}")

print("\n---------------Exercise5---------------")

while True:
    try:
        origin_strand = input("Enter the origin DNA strand: ").upper()
        complementary_strand = dna_complement(origin_strand)
        print(f"Complementary strand: {complementary_strand}")
        break

    except ValueError as e:
        print(f"Error: {e}")
