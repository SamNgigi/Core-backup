print("if statements");
height = 74#heights in inches
if height > 70 :
    print("Bruv you tall");

# Checking for multiple conditions
print("");
print("multiple conditions");
height = 68;
if height>70:
    print("You tall bruv");
elif height> 60:
    print("Uko average bruv");
else:
    print("Uko short!");

# In Python an empty value is automatically considered to be false.
# print("");
# print("Returning empty values");
# name = "";
# list_a = [];
#
# if list_a:
#     print("I will not run");
# else:
#     print("I am kinda empty");

# Loops
print("");
print("Looping listing normally using an array/list style");
numbers = [1,2,3,4,5]
for number in numbers:
    print(number);
# List in an array like style
print("");
print("Looping using range");
list_a = list(range(0,6));
print(list_a);
# Below is another really cool application of range()
print("");
print("Using counter variable");
for number in range(0,7):
    print("Bruv give me "+ str(number)+" samosas")
# For loop wiht conditions
numbers = [1,2,3,4,5];
for number in numbers:
    if number % 2 == 0:
        print(number);
