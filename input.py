import sys
# The below code allows us to pass in arguments from the command line.
# So executing this python program we can type in our name say Sam before executing it. And our name will be stored to the name variable through the sys.argva[].
# Literally we can take sys.argv[] to mean system.argument variable.

name = sys.argv[1]

print("How old are you?")
age = int(input())

print(name)
print(age)
