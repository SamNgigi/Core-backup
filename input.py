print("What is your name?");
name = input();

print("What is your age?");
# int() is to convert the inputfrom string into number.
age = int(input());


# Have to convert int into string using str(age)
print("Hi " + name + ".Looking good for " + str(age) + " years young :)")
