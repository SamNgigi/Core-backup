text_file = "tests.txt"


def read_file(text_file):
    '''
    function that reads a text file and returns the data from the text file
    '''
    with open(text_file, "r") as handle:
        data = handle.read()
        return data


def read_file(text_file):
    """
    Function that reads a text file and returns the data from the text file

    Raises:
        FileNotFoundError:If it cannot the file
    """

    try:
        with open(text_file, "r") as handle:

            data = handle.read()
            return data
    except FileNotFoundError:

        return None


def word_count(text_file):
    count = 0
    for word in read_file(text_file).split():
        if word == "Moringa":
            count += 1
    return count


def line_count(text_file):
    with open(text_file) as handle:
        jina = handle.readlines()
        lines_zetu = len(jina)

    return lines_zetu

# def longest_inString(text_file):
#     with open (text_file) as handle:
#         data = handle.read()
#         long_word = ""
#         for word in data.split():
#             if word > long_word:
#                 long_word = word
#                 return long_word
