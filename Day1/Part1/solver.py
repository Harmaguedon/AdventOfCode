#! /usr/bin/python3

with open('./inputs', 'r') as inputs:
    inputs = [ int(input.strip()) for input in inputs.readlines()]
    oldValue = None
    count = 0
    for value in inputs:
        if oldValue is not None and oldValue < value:
            count += 1
        oldValue = value
    print(count)

