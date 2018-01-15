

# clicks = []
# list_one= [a,d,g,j,m,p,t,w]
# list_two = [b,e,h,k,n,q,u,x]
# list_three = [c,f,i,l,o,r,v,y]
# list_four = [s,z]


 # or


#     if char == i in list_one:
#         return x = 1
# elif char == i in list_two:
#     return y = 2
# elif char == i in list_3:
#     return z = 3
# elif char == i in list_4:
#     return a = 4;
#
# print(a+x+z+y)
print("Enter a string")

input_string = input()
list_one= ["a","d","g","j","m","p","t","w"," ", "1"]
list_two = ["b","e","h","k","n","q","u","x"]
list_three = ["c","f","i","l","o","r","v","y"]
list_four = ["s","z"]



x=0;
for i in input_string:
    if i in list_one:
        x += 1
        # print(i)
    elif i in list_two:
        x += 1* 2
        # print(i)
    elif i in list_three:
        x += 1* 3
        # print(i)
    elif i in list_four:
        x += 1* 4
        # print(i)
    else:
     print("enter a string!")

print(str(x))



# for character in input_string:
#     characters.setdefault(character,0)
#     characters[character] = characters[character] + 1


# for character in input_string:
#     characters.setdefault(character,0)
#     characters[character] = characters[character] + 1

# print(characters)
