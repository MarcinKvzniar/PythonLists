import unittest
from biological_sequences import DNASequence, RNASequence, ProteinSequence


class TestDNSequence(unittest.TestCase):

    def setUp(self):
        self.valid_dna = DNASequence("ATGCGTACG", "dna_seq_1")
        self.invalid_dna = DNASequence("UAG42CGTAC", "dna_seq_2")

    def test_len(self):
        self.assertEqual(len(self.valid_dna), 9)

    def test_str(self):
        self.assertEqual(str(self.valid_dna), ">dna_seq_1 \n ATGCGTACG")

    def test_mutate_valid(self):
        mutated_seq = self.valid_dna.mutate(2, 'C')
        self.assertEqual(mutated_seq, "ATCGCGTACG")

    def test_mutate_invalid_position(self):
        with self.assertRaises(ValueError):
            self.valid_dna.mutate(10, 'C')
            self.valid_dna.mutate('c', 'C')

    def test_mutate_invalid_value(self):
        with self.assertRaises(ValueError):
            self.valid_dna.mutate(2, 'U')
            self.valid_dna.mutate(2, 4)

    def test_find_motif(self):
        self.assertEqual(self.valid_dna.find_motif("AG"), [])
        self.assertEqual(self.valid_dna.find_motif("TG"), [(1, 2)])
        self.assertEqual(self.valid_dna.find_motif("CG"), [(3, 4), (7, 8)])

    def test_complement_valid(self):
        self.assertEqual(self.valid_dna.complement(), "TACGCATGC")

    def test_complement_invalid(self):
        with self.assertRaises(ValueError):
            self.invalid_dna.complement()

    def test_transcribe_valid(self):
        transcribed_rna = self.valid_dna.transcribe()
        self.assertEqual(transcribed_rna.data, "AUGCGUACG")
        self.assertIsInstance(transcribed_rna, RNASequence)

    def test_transcribe_invalid(self):
        with self.assertRaises(ValueError):
            self.invalid_dna.transcribe()


class TestRNASequence(unittest.TestCase):

    def setUp(self):
        self.valid_rna = RNASequence("CUGAGGGUG", "rna_seq_1")
        self.invalid_rna = RNASequence("A42CBGUCAU", "rna_seq_2")

    def test_len(self):
        self.assertEqual(len(self.valid_rna), 9)

    def test_str(self):
        self.assertEqual(str(self.valid_rna), ">rna_seq_1 \n CUGAGGGUG")

    def test_mutate_valid(self):
        mutated_seq = self.valid_rna.mutate(2, 'C')
        self.assertEqual(mutated_seq, "CUCGAGGGUG")

    def test_mutate_invalid_position(self):
        with self.assertRaises(ValueError):
            self.valid_rna.mutate(10, 'U')
            self.valid_rna.mutate('X', 'U')

    def test_mutate_invalid_value(self):
        with self.assertRaises(ValueError):
            self.valid_rna.mutate(2, 'X')
            self.valid_rna.mutate(2, 4)

    def test_complement_valid(self):
        self.assertEqual(self.valid_rna.complement(), "GACUCCCAC")

    def test_complement_invalid(self):
        with self.assertRaises(ValueError):
            self.invalid_rna.complement()

    def test_translate_valid(self):
        translated_protein = self.valid_rna.translate()
        self.assertEqual(translated_protein.data, "LRV")
        self.assertIsInstance(translated_protein, ProteinSequence)

    def test_translate_invalid(self):
        with self.assertRaises(ValueError):
            self.invalid_rna.translate()


class TestProteinSequence(unittest.TestCase):

    def setUp(self):
        self.valid_protein = ProteinSequence("ACDEFGHIKLMNPQRSTVWY", "protein_seq_1")
        self.invalid_protein = ProteinSequence("A42CBXFGHIKLMN526PQRSTVWY", "protein_seq_2")

    def test_len(self):
        self.assertEqual(len(self.valid_protein), 20)

    def test_str(self):
        self.assertEqual(str(self.valid_protein), ">protein_seq_1 \n ACDEFGHIKLMNPQRSTVWY")

    def test_mutate_valid(self):
        mutated_seq = self.valid_protein.mutate(2, 'C')
        self.assertEqual(mutated_seq, "ACCDEFGHIKLMNPQRSTVWY")

    def test_mutate_invalid_position(self):
        with self.assertRaises(ValueError):
            self.valid_protein.mutate(10, 'U')
            self.valid_protein.mutate('X', 'U')

    def test_mutate_invalid_value(self):
        with self.assertRaises(ValueError):
            self.valid_protein.mutate(2, 'X')
            self.valid_protein.mutate(2, 4)

    def test_find_motif(self):
        self.assertEqual(self.valid_protein.find_motif("ADC"), [])
        self.assertEqual(self.valid_protein.find_motif("FGH"), [(4, 6)])

    def test_find_motif_invalid(self):
        with self.assertRaises(ValueError):
            self.invalid_protein.find_motif("F4H")


if __name__ == '__main__':
    unittest.main()
