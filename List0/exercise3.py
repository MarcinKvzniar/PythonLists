def fibonacci(n):
    # we are checking if the number is a bigger than 0 integer, if not we are raising ValueError
    if n < 0 or not isinstance(n, int):
        raise ValueError("n has to be an integer >=  0")

    a = 0
    b = 1

# if n is equal to 0 we return 0, if equal to 1 we return 1, else we use fibonacci algorithm
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2, n+1):     # we are iterating between 2 and n (n+1 is being excluded)
            temp = a                # we create temporary variable that stores our a value
            a = b                   # we assign value of b to a
            b += temp               # we assign the sum of b and initial value of a to b
        return b


def test_fibonacci():
    # Test cases
    assert fibonacci(0) == 0, "Test case 1 failed"
    assert fibonacci(1) == 1, "Test case 2 failed"
    assert fibonacci(5) == 5, "Test case 3 failed"
    assert fibonacci(10) == 55, "Test case 4 failed"

    # Test with a negative input
    try:
        fibonacci(-1)
    except ValueError:
        pass
    else:
        assert False, "Test case 5 failed"

    # Test with a non-integer input
    try:
        fibonacci(0.07)
    except ValueError:
        pass
    else:
        assert False, "Test case 6 failed"

    print("All tests passed successfully")


try:
    n = int(input("Enter the element of fibonacci sequence that you want to know the value of: "))
    print(f"The {n} element of Fibonacci sequence is: {fibonacci(n)}")
except ValueError as e:
    print(f"Error: {e}")

test_fibonacci()
