#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        n = len(list)
        for i in range(n):
            if i != (n - 1):
                print("{:d}".format(list[i]), end=' ')
            else:
                print("{:d}".format(list[i]))
