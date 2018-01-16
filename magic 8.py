import random


i = 0
while i < 2:
    user = input("Ask me anything you want: ")
    random_number = random.randint(0, 1)
    print(random_number)

    if random_number == 1:
        print("HA! You're joking right..? Of course NOT")
    else:
        print("..You crazy my G")
    i += 1


# Using and combining logical operators
print("are you sick? y/n")
ans = input()
# print(ans)
random_number = random.randint(1, 3)

if ans.isalpha() and ans == "y" or ans == "n":
    print("you entered correctly")
    if random_number == 1:
        print("you are gangsta")
    elif random_number == 2:
        print("you are the cool")
# elif random_number == 3:
#     print("you are the bomb.com")
# elif random_number == 4:
#     print("you are a conman")
# elif random_number == 5:
#     print("you are tricky")
# elif random_number == 6:
#         print("you are complicated")
# elif random_number == 7:
#     print("you are smart")
# elif random_number == 8:
#     print("you are logical")
else:
    print("error 404!!!!")
