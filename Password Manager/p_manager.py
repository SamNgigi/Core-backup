#!/usr/bin/env python3.6
"""
1.Generate password
2.Save password
3.Tear Down
4.Save multiple
5.Delete password profile
6.Display
7.Find by profile
8.Copy_paste
"""
import random

print("How long do you want your password:")
password_length = int(input())
string = "abcdefghigjkmnopqrstuvwxyz1234567890-_=+{}\|"';>./,`!@#$%^&*()`'
password = "".join(random.sample(string, password_length))
print(password)
