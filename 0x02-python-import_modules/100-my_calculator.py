#!/usr/bin/python3
from calculator_1 import mul, add, div, sub
from sys import argv, exit

n = len(argv) - 1
operators = ['+', '-', '*', '/']
a = int(argv[1])
b = int(argv[3])
opp = argv[2]

if __name__ == "__main__":
    if (n != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if (opp not in operators):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if opp == '+':
        print(f"{a} {opp} {b} = {add(a, b)}")
    elif opp == '-':
        print(f"{a} {opp} {b} = {sub(a, b)}")
    elif opp == '*':
        print(f"{a} {opp} {b} = {mul(a, b)}")
    elif opp == '/':
        print(f"{a} {opp} {b} = {div(a, b)}")
