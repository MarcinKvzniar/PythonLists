def is_in_list_rec(x, T):
    """
    This function checks if x is in list T using recursion.

    Arguments:
         x - element to be found
         T - list of elements
    Returns:
        True if x is in T, False otherwise
    """
    if len(T) == 0:
        return False
    if T[0] == x:
        return True
    else:
        return is_in_list_rec(x, T[1:])


def binary_search_rec(T, x, start, end):
    """
    This function searches for x in list T using binary search algorithm
    and recursion.

    Arguments:
        T - list of elements
        x - element to be found
        start - start index
        end - end index
    Returns:
        index of x in T if x is in T, None otherwise
    """
    if start > end:
        return None

    center = (start + end) // 2

    if T[center] == x:
        return center
    elif T[center] > x:
        return binary_search_rec(T, x, start, center - 1)
    else:
        return binary_search_rec(T, x, center + 1, end)


if __name__ == '__main__':
    T = [-2, 1, 1.0, 3, 8]

    print("Task 1: ")
    print(is_in_list_rec(0, T))     # False
    print(is_in_list_rec(3, T))     # True
    print(is_in_list_rec(-2, T))       # True
    print(is_in_list_rec(8, T))     # True
    print(is_in_list_rec(1, T))     # True
    print(is_in_list_rec(T, []))    # False

    print("\nTask 2: ")
    print(binary_search_rec(T, 0, 0, len(T) - 1))    # None
    print(binary_search_rec(T, 1, 0, len(T) - 1))    # 2
    print(binary_search_rec(T, -2, 0, len(T) - 1))      # 0
    print(binary_search_rec(T, 8.0, 0, len(T) - 1))  # 4



