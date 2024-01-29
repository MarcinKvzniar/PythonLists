def seq_validator_gen(alphabet):
    def seq_validator(seq):
        for letter in seq:
            if letter not in alphabet:
                return False
        return True

    return seq_validator


if __name__ == '__main__':
    print("Task 1:")
    dna_validator = seq_validator_gen(['A', 'C', 'G', 'T'])

    print(dna_validator('TTGCTAAGG'))

    print(dna_validator('UUGCUAAGG'))

    print("\nTask 2:")
