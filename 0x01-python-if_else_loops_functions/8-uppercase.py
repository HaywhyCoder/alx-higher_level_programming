#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if (ord(char) in range(65, 91)):
            continue
        elif (ord(char) in range(97, 123)):
            asci = ord(char)
            char = chr(asci - 32)

    print("{}".format(str))
