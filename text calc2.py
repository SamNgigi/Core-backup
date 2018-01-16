

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
list_one= ["a","d","g","j","m","p","t","w"," ","1","*","#"]
list_two = ["b","e","h","k","n","q","u","x"]
list_three = ["c","f","i","l","o","r","v","y"]
list_four = ["s","z","2","3","4","5","6","8"]
list_five = ["7","9"]



x=0;
if input_string =="":
    print("enter a number!")
else:
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
        elif i in list_five:
            x += 1* 5
            # print(i)
    print(str(x))



# for character in input_string:
#     characters.setdefault(character,0)
#     characters[character] = characters[character] + 1


# for character in input_string:
#     characters.setdefault(character,0)
#     characters[character] = characters[character] + 1

# print(characters)
