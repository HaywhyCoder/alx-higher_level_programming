#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if (ord(char) in range(65, 91)):
            continue
        elif (ord(char) in range(97, 123)):
            asci = ord(char)
            char = chr(asci - 32)

count = 3
while count > 0:
    x = input("> ")
    print(uppercase(x))
    count -= 1
