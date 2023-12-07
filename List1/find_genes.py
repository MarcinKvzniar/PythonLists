def find_genes(dna_string):
    """
    This function searches for potential genes in a sequence of codons
    and returns identified genes as a list

    Arguments:
        dna_string (str): A string that represents the DNA sequence to
                          search for potential genes.

    Returns:
        potential_genes: A list of potential genes identified within
                         the DNA sequence.

    Raises:
        ValueError: If any of these conditions are not me:
            - it doesn't start with the start codon ATG
            - it contains signs that not represent a DNA string
            - it doesn't end with a stop codon
            - its length is not a multiple of 3
            - it contains intervening stop codons
            - it does not have any potential genes
    """
    valid_bases = set('ACGT')
    beginning_code = "ATG"
    end_codes = ["TAG", "TAA", "TGA"]
    potential_genes = []

    for base in valid_bases:
        if base not in valid_bases:
            raise ValueError("This is not a DNA sequence")

    if len(dna_string) % 3 != 0:
        raise ValueError("Given DNA string length is not a multiple of 3")
    elif dna_string[0:3] != beginning_code:
        raise ValueError("Given DNA does not start with the start codon ATG")
    elif dna_string[-3:] not in end_codes:
        raise ValueError("Given DNA does not end with any of the stop codons")

    for code in end_codes:
        if dna_string.count(code) > 1:
            raise ValueError("Given DNA has more than one stop codon")

    for i in range(len(dna_string)):
        for j in range(i + 3, len(dna_string), 3):
            if dna_string[j:j + 3] in end_codes:
                potential_genes.append(dna_string[i:j + 3])
                break

    if not potential_genes:
        raise ValueError("No potential genes found in the given DNA sequence.")

    return potential_genes


try:
    dna_string = input("Insert gene: ").upper()
    check_dna_string = find_genes(dna_string)
    print(f"Potential genes found: {check_dna_string}")
except ValueError as e:
    print(f"Error: {e}")
