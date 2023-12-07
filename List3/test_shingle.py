import unittest
from unittest.mock import patch
import tempfile
import sys
import os
import shingle


class TestShingle(unittest.TestCase):

    def test_main_with_file(self):
        """
        The idea and implementation was developed with the help of
        'Chat Bing with GPT-4', since my first test method with the
        usage of import mock_open from unittest.mock package required
        to provide a directory to already existing text file.
        This one creates a sample text file that contains a message
        from variable 'message'.
        """
        # test with valid file input
        with tempfile.NamedTemporaryFile(delete=False) as temp:
            message = "test text: one two three, four! one two one two"
            temp.write(message.encode())
            temp.close()
            test_args = ["compare.py", "-n", "20", "-k", "2",
                         "-file", temp.name]
            with patch.object(sys, 'argv', test_args):
                shingle.main()
        os.remove(temp.name)

    def test_main_without_file(self):
        # test with valid console input
        test_args = ["compare.py", "-n", "20", "-k", "2"]
        input_data = ["line1", "line2", "line3", EOFError]
        with (patch.object(sys, 'argv', test_args),
              patch('builtins.input', side_effect=input_data)):
            shingle.main()

    def test_main_with_invalid_n(self):
        # test with invalid n (not bigger than 0)
        test_args = ["compare.py", "-n", "0", "-k", "2"]
        with patch.object(sys, 'argv', test_args):
            self.assertRaises(ValueError, shingle.main)

    def test_main_with_invalid_k(self):
        # test with invalid k (not bigger than 0)
        test_args = ["compare.py", "-n", "20", "-k", "0"]
        with patch.object(sys, 'argv', test_args):
            self.assertRaises(ValueError, shingle.main)


if __name__ == '__main__':
    unittest.main()
