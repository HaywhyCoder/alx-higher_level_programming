#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    n = len(argv) - 1
    if n == 0:
        end = '.'
    else:
        end = ':'
    if n == 1:
        arg = "argument"
    else:
        arg = "arguments"
    print("{} {}{}".format(n, arg, end))
    for i in range(1, n + 1):
        print("{}{} {}".format(i, end, argv[i]))
