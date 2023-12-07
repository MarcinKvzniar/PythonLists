class Sequence:
    valid_chars = set('')

    def __init__(self, data, identifier):
        self.identifier = identifier
        self.data = data

    def __len__(self):
        """
        This function calculates the length of a particular strand

        Returns:
            len(self.data) (int): length of a strand
        """
        return len(self.data)

    def __str__(self):
        """
        This function implements representation in the FASTA-like format

        Returns:
            data in FAST-like format
        """
        return f">{self.identifier} \n {self.data}"

    def mutate(self, position, value):
        """
        This function modifies sequence at a given position by a
        provided value

        Arguments:
            position (int): Position in strand at which mutation occurs
            value (str): Value that is inserted at a provided position

        Returns:
            data_mutated: Mutated strand

        Raises:
            ValueError: If provided position is not an integer or is
                        out of the range given by strand's length
                        If provided value is not in valid chars
        """
        if (not 0 <= position < len(self.data)
                or not isinstance(position, int)):
            raise ValueError("Invalid position provided")

        for base in value:
            if base not in self.valid_chars:
                raise ValueError("Invalid value provided")

        data_mutated = self.data[:position] + value + self.data[position:]
        return data_mutated


class DNASequence(Sequence):

    def __init__(self, data, identifier):
        super().__init__(data, identifier)
        self.valid_chars = set('ACTG')

    def find_motif(self, motif):
        """
        This function finds positions of the given motifs in a
        DNA sequence

        Arguments:
            motif: motif that has to be found in the strand

        Returns:
            motif_positions (list of tuples): a list of positions
                where a given motif occurs

        Raises:
            ValueError: If the invalid motif was provided
        """

        for char in motif:
            if char not in self.valid_chars:
                raise ValueError("Invalid motif provided.")

        motif_length = len(motif)
        motif_positions = []

        for i in range(len(self.data) - motif_length + 1):
            if self.data[i:i + motif_length] == motif:
                motif_start_pos = i
                motif_end_pos = i + motif_length - 1
                occurrence = (motif_start_pos, motif_end_pos)
                motif_positions.append(occurrence)

        return motif_positions

    def complement(self):
        """
        This function creates a complementary DNA strand to the
            provided one

        Returns:
            comp_data (str): A complementary strand

        Raises:
            ValueError: If any base of the origin strand does not belong
                to valid chars
        """
        comp_data = ""
        for base in self.data:
            if base not in self.valid_chars:
                raise ValueError("Invalid value provided.")

            if base == 'A':
                comp_data += 'T'

            elif base == 'T':
                comp_data += 'A'

            elif base == 'C':
                comp_data += 'G'

            elif base == 'G':
                comp_data += 'C'

        return comp_data

    def transcribe(self):
        """
        This function transcribes a DNA strand to RNA

        Returns:
            Transcribed strand - an object of class RNASequence

        Raises:
            ValueError: If any base of the origin strand does not belong
                to valid chars
        """
        for base in self.data:
            if base not in self.valid_chars:
                raise ValueError("Invalid value provided.")

        transcribed_sequence = self.data.replace('T', 'U')

        return RNASequence(transcribed_sequence, self.identifier)


class RNASequence(Sequence):
    codon_map = {
        "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
        "UAU": "Y", "UAC": "Y", "UAA": "STOP", "UAG": "STOP",
        "UGU": "C", "UGC": "C", "UGA": "STOP", "UGG": "W",
        "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
        "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
        "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
    }

    def __init__(self, data, identifier):
        super().__init__(data, identifier)
        self.valid_chars = set('ACUG')

    def complement(self):
        """
        This function creates a complementary RNA strand to the
            provided one

        Returns:
            comp_data (str): A complementary strand

        Raises:
            ValueError: If any base of the origin strand does not belong
                to valid chars
        """
        comp_data = ""
        for base in self.data:
            if base not in self.valid_chars:
                raise ValueError("Invalid value provided.")

            if base == 'A':
                comp_data += 'U'

            elif base == 'U':
                comp_data += 'A'

            elif base == 'C':
                comp_data += 'G'

            elif base == 'G':
                comp_data += 'C'

        return comp_data

    def translate(self):
        """
        This function translates RNA strand to a protein sequence

        Returns:
            translated_sequence - an object of class ProteinSequence

        Raises:
            ValueError: If any codon of the origin strand does not belong
                to codons map
        """
        codons = []

        for i in range(0, len(self.data), 3):
            codon = self.data[i: i + 3]
            codons.append(codon)

        translated_sequence = ""

        for codon in codons:
            if codon not in self.codon_map:
                raise ValueError("Invalid codon found in the sequence.")

            if codon in self.codon_map:
                amino_acid = self.codon_map[codon]
                if amino_acid == "STOP":
                    break
                translated_sequence += amino_acid

        return ProteinSequence(translated_sequence, self.identifier)


class ProteinSequence(Sequence):

    def __init__(self, data, identifier):
        super().__init__(data, identifier)
        self.valid_chars = set('ACDEFGHIKLMNPQRSTVWY')

    def find_motif(self, motif):
        """
        This function finds positions of the given motifs in a
        Protein sequence

        Arguments:
            motif: motif that has to be found in the strand

        Returns:
            motif_positions (list of tuples): a list of positions
                where a given motif occurs

        Raises:
            ValueError: If the invalid motif was provided
        """
        for char in motif:
            if char not in self.valid_chars:
                raise ValueError("Invalid motif provided.")

        motif_length = len(motif)
        motif_positions = []

        for i in range(len(self.data) - motif_length + 1):
            if self.data[i:i + motif_length] == motif:
                motif_start_pos = i
                motif_end_pos = i + motif_length - 1
                occurrence = (motif_start_pos, motif_end_pos)
                motif_positions.append(occurrence)

        return motif_positions


if __name__ == '__main__':

    print("########### ")
    print("DNA sequence functionality: ")
    print("########### \n")

    dna_strand = DNASequence("ATCGGCTAATCGAAGCT", 'HumanDNA')

    length_dna = len(dna_strand)
    print(f"The length of this strand is: {length_dna} \n")

    string_dna = str(dna_strand)
    print(f"The representation in the FASTA-like format"
          f" is: \n {string_dna} \n")

    mutation_dna = DNASequence.mutate(dna_strand, 4, 'CCC')
    print(f"This strand after mutation is: {mutation_dna} \n")

    motif_dna = DNASequence.find_motif(dna_strand, 'GCT')
    print(f"Positions of the provided motif found in this strand:"
          f" {motif_dna} \n")

    comp_strand_dna = DNASequence.complement(dna_strand)
    print(f"Complementary strand to the provided one:"
          f" {comp_strand_dna} \n")

    transcribed_strand_dna = DNASequence.transcribe(dna_strand)
    print(f"This strand transcribed to RNA is:"
          f" \n {transcribed_strand_dna} \n")

    print("###########")
    print("RNA sequence functionality: ")
    print("###########\n")

    rna_strand = RNASequence('UUUUUACUGAGGGUG', 'COVID_RNA')

    length_rna = len(rna_strand)
    print(f"The length of this strand is: {length_rna} \n")

    string_rna = str(rna_strand)
    print(f"The representation in the FASTA-like format"
          f" is: \n {string_rna} \n")

    mutation_rna = RNASequence.mutate(rna_strand, 4, 'CCC')
    print(f"This strand after mutation is: {mutation_rna} \n")

    comp_strand_rna = RNASequence.complement(rna_strand)
    print(f"Complementary strand to the provided one:"
          f" {comp_strand_rna} \n")

    translated_strand_rna = RNASequence.translate(rna_strand)
    print(f"This strand translated to protein sequence is:"
          f" \n {translated_strand_rna} \n")

    print("###########")
    print("Protein sequence functionality: ")
    print("########### \n")

    protein_strand = ProteinSequence("MSRSLLLRFLLFLLLLPPLP",
                                     "Hemoglobin")

    length_protein = len(protein_strand)
    print(f"The length of this strand is: {length_protein} \n")

    string_protein = str(protein_strand)
    print(f"The representation in the FASTA-like format"
          f" is: \n {string_protein} \n")

    mutation_protein = ProteinSequence.mutate(protein_strand,
                                              4, 'CCC')
    print(f"This strand after mutation is: {mutation_protein} \n")

    motif_protein = ProteinSequence.find_motif(protein_strand, 'LLL')
    print(f"Positions of the provided motif found in this strand:"
          f" {motif_protein} \n")







