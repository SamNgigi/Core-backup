"""
Seems that there is no need for creating a class if we are not
working with a list of properties and functions
"""
# read_list = []

text_file = "tests.txt"


def file_read(text_file):
    """
    Function that reads a text file and returns the data from the text file

    We pass in text_file parameter as a placeholder where
    we can store our actual text file when calling this function.

    It raises:
    FileNotFoundError:if it cannot find the file
    """
    try:
        with open(text_file, "r") as handle:
            data = handle.read()
            return data
    except FileNotFoundError:
        return None
