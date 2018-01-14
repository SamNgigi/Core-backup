import this
# import math

# importing like above we would have to type the module name -math- when we want to use it.
# The below way of importing we can ommit the module name.
from math import sqrt, ceil

# We can generate random numbers using the randInt
import random


# math --> module
# .sqrt()/ceil() --> module method.
# (9) --> parameters


print("");
x = sqrt(9);
print(x);
# Whole number without a decimal Rounding up.


y = ceil(x);
print(y);

# For displaying the random numbers
print("");
print("Random numbers using random module")
random_number = random.randint(0,10);
print(random_number);


# Circumference Calculation
print("");
print("Circumference")
radius = random.randint(0,10);
circumference = 2*3.14*radius;
print(circumference);
