def divisible(numbers, divisor):
    numbers_div = []  # we are creating an empty list
    for num in numbers:  # iterating through every number in the list of numbers
        if num % divisor == 0:  # if a number is divisible by a divisor without rest
            numbers_div.append(num)  # we are adding it to the list of numbers

    return numbers_div


def test_divisible():
    # Test cases
    result1 = divisible([1, 2, 3, 4, 5, 6, 9], 3)
    assert result1 == [3, 6, 9], "Test case 1 failed"

    result2 = divisible([10, 20, 30, 40, 5, 21], 9)
    assert result2 == [], "Test case 2 failed"

    result3 = divisible([], 10)
    assert result3 == [], "Test case 3 failed"

    result4 = divisible([10, 20, 30, 40, 50], 10)
    assert result4 == [10, 20, 30, 40, 50], "Test case 4 failed"

    print("All the tests passed successfully")


print(divisible([1, 2, 3, 4, 5, 6, 9], 3))
test_divisible()
