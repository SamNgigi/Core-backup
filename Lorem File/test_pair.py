import unittest
import readfiles


class TestReadFiles(unittest.TestCase):

    def test_get_data(self):
        '''
        Test case to confirm we are getting data from the file
        '''
        with open("test.txt", "r") as handle:
            data = handle.read()
            self.assertEqual(data, readfiles.read_file('test.txt'))

    def test_nonfile(self):
        """
        Test to confirm that an exeption is raised when a wrong file is inputted
        """
        self.assertEqual(None, readfiles.read_file("tests.txt"))

    def test_word_count(self):
        with open("test.txt", "r") as handle:
            data = handle.read()
            counter = 0
            for word in data.split():
                if word == "Moringa":
                    counter += 1
            # print(str(counter))

        self.assertEqual(counter, readfiles.word_count('test.txt'))
        print(str(counter))
        print(str(readfiles.word_count('test.txt')))

    def test_line_count(self):
        with open("test.txt") as handle:
            data = handle.readlines()
            lines = len(data)
            # print(lines)
        self.assertEqual(lines, readfiles.line_count('test.txt'))

    def test_longest_inString(self):
        with open("test.txt") as handle:
            data = handle.read()
            longest_word = ""
            for word in data.split():
                if len(word) > len(longest_word):
                    longest_word = word
            print(longest_word)
            #   return longest_word

    #    self.assertEqual(longest_word, long_word)


if __name__ == "__main__":
    unittest.main()
