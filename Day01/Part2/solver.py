#! /usr/bin/python3

with open('./inputs', 'r') as inputs:
    inputs = [ int(input.strip()) for input in inputs.readlines()]
    slidingWindowInputs = [ sum(inputs[i:i+3]) for i in range(0,len(inputs)-2) ]
    oldValue = None
    count = 0
    for value in slidingWindowInputs:
        if oldValue is not None and oldValue < value:
            count += 1
        oldValue = value
    print(count)
