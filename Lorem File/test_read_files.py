#!/usr/bin/env python3.6
import unittest
import read_files


class TestReadFiles(unittest.TestCase):
    """
    Class to test the functions on the read_files module(scripts)

    Args:
    unittest.TestCase: Class from the unittest module to create unit tests
    """

    def test_get_data(self):
        """
        Test case to confirm that we are getting data from the file
        """
        with open("test.txt", "r") as handle:
            data = handle.read()
            self.assertEqual(data, read_files.file_read("test.txt"))

    def test_wrong_file(self):
        """
        Test to confirm that an exeption is raised when a
        wrong file is inputted.
        """
        self.assertEqual(None, read_files.file_read("tests.txt"))

    def test_word_times(self):
        """
        Test to confirm if we can look for a certain word.
        Here we want
        """
        with open("test.txt", "r") as handle:
            data = handle.read()
            word_count = self.data.


if __name__ == "__main__":
    unittest.main()
