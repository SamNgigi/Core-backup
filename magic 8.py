import random



i = 0
while i < 2:
    user = input("Ask me anything you want: ");
    random_number = random.randint(0,1);
    print(random_number)

    if random_number ==  1:
           print("HA! You're joking right..? Of course NOT");
    else:
              print ("..You crazy my G")
    i += 1
