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


if __name__ == "__main__":
    unittest.main()
