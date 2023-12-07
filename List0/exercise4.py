def vowel_counter(string):
    string = string.lower()
    count = 0
    vowels = set("aeiouy")
    for char in string:
        if char in vowels:
            count += 1
    return count


string = str(input("Enter some string: "))

print(f"Original string: {string}")
print(f"Length of the string: {len(string)}")
print(f"Reversed string: {string[::-1]}")
print(f"Number of vowels: {vowel_counter(string)}")
