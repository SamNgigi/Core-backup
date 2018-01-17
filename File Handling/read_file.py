#!/usr/bin/env python3.6

#
# There are two types of text files
# 1. Text files - organized sequence of lines that include characters.
# 2. Binary files -not text file. Have encoding and a method to be read.
#
# The open() function allows us to read files.
# e.g.
#  example = open("filename","mode");
#  mode --> r - read
#       --> w - write
#       --> a - append
#       --> r+ - read and write
#

handle = open("text.txt", "r")
# below we store the read file in handle in data.
# Then use read() to read the whole file
data = handle.read()
print("All the text")
print("")
print(data)

# We use readline() to read one single line
handle2 = open("text.txt", "r")
oner = handle2.readline()
print("Just the top line")
print("")
print(oner)

# readlines() returns array/list of all the lines in our file separetad by \n.
handle3 = open("text.txt")  # Default mode is r
string_list = handle3.readlines()
print("The array")
print("")
print(string_list)
# We the then use the .close() method to close the file handle because,

handle4 = open("text.txt")
find_word = handle4.read()
counter = 0
for word in data.split():
    if word == "Python":
        counter += 1
print("")
print(f"The word Python in the text.txt occurs {counter} times")
# print(str(counter) + " times")


handle.close()
