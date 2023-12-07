import os
import sys
import unittest
from unittest.mock import patch
import tempfile
import compare


class TestCompare(unittest.TestCase):

    def test_jaccard_similarity(self):
        # test case for scenario when both sets are empty
        self.assertRaises(ValueError, compare.jaccard_similarity, {}, {})

        # test case for scenario when one set is empty
        self.assertRaises(ValueError, compare.jaccard_similarity,
                          {"test": 1}, {})

        # test cases for scenarios when inputs are not dictionaries
        self.assertRaises(TypeError, compare.jaccard_similarity, 4, {})
        self.assertRaises(TypeError, compare.jaccard_similarity, {}, 'abc')
        self.assertRaises(TypeError, compare.jaccard_similarity, 4, 'abc')
        self.assertRaises(TypeError, compare.jaccard_similarity, [], [])

        # test case for a common scenario
        self.assertEqual(compare.jaccard_similarity({("test", "case"): 2,
                                                     ("case", "one"): 1},
                                                    {("test", "case"): 1,
                                                     ("test", "one"): 1}), 0.25)

        # test case for scenario when both sets have no common elements
        self.assertEqual(compare.jaccard_similarity({("test", "case"): 1,
                                                     ("text", "one"): 1},
                                                    {("text", "case"): 1,
                                                     ("test", "one"): 1}), 0)

        # test case for scenario when both sets have common elements
        self.assertEqual(compare.jaccard_similarity({("test", "case"): 1,
                                                     ("text", "one"): 1},
                                                    {("test", "case"): 1,
                                                     ("text", "one"): 1}), 1.0)

    def test_main(self):
        """
        Same annotation as in case of function test_main_with_file
        in module test_shingles.py
        """
        with tempfile.NamedTemporaryFile(delete=False) as temp_query:
            with tempfile.NamedTemporaryFile(delete=False) as temp_target:
                temp_query.write(b"test text one")
                temp_target.write(b"test, text: one!")

                temp_query.close()
                temp_target.close()

                # test case for scenario when remove_punctuation is set to False
                test_args = ["compare.py", "--query", temp_query.name,
                             "--target", temp_target.name,
                             "-k", "2"]
                with patch.object(sys, 'argv', test_args):
                    compare.main()

                # test case for scenario when remove_punctuation is set to True
                test_args = ["compare.py", "--query", temp_query.name,
                             "--target", temp_target.name,
                             "-k", "2",
                             "--remove_punctuation"]
                with patch.object(sys, 'argv', test_args):
                    compare.main()

        os.remove(temp_query.name)
        os.remove(temp_target.name)


if __name__ == '__main__':
    unittest.main()
