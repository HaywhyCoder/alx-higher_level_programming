#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        firstChr = None
    else:
        firstChr = sentence[0]
    return (length, firstChr)
