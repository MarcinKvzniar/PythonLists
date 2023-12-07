from list1 import weekday, segment_length, dec2bin, dna_complement

# Test for the weekday function
assert weekday(14, 10, 2023) == 6, \
    "Test case 1 (valid input) for function weekday has failed"

try:
    weekday(-12, 27, 0)
except ValueError:
    pass
else:
    assert False, ("Test case 2 (provided numbers are out of ranges)"
                   " for function weekday has failed")

try:
    weekday('A', '-', 3.84)
except ValueError:
    pass
else:
    assert False, ("Test case 3 (non-integer numbers provided)"
                   " for function weekday has failed")

# Test for the segment_length function
assert segment_length(3, 7, 5, 9) == (5, 7), \
    ("Test case 1 (valid input returning intersection) for function "
     "segment_length has failed")
assert segment_length(7, 5, 9, 5) is None,\
    ("Test case 2 (valid input returning None) for function"
     " segment_length has failed")

try:
    segment_length('A', -3, 'B', 0)
except ValueError:
    pass
else:
    assert False, ("Test case 3 (provided numbers are not numbers)"
                   " for function segment_length has failed")

# Test for the dec2bin function
assert dec2bin(42) == '0 101010',\
    "Test case 1 (valid positive input) for function dec2bin has failed"

assert dec2bin(-23) == '1 10111',\
    "Test case 2 (valid negative input) for function dec2bin has failed"

assert dec2bin(0) == '0',\
    "Test case 3 (0 input) for function dec2bin has failed"

try:
    dec2bin('A')
except ValueError:
    pass
else:
    assert False, ("Test case 4 (non-integer input)"
                   " for function dec2bin has failed")

# Test for the dna_complement function
assert dna_complement('ATCG') == 'TAGC',\
    "Test case 1 for function dna_complement has failed"

try:
    dna_complement('ATCGB4')
except ValueError:
    pass
else:
    assert False, "Test case 2 for function dna_complement has failed"

print("\nAll tests passed successfully!")
