#! /usr/bin/python3

with open('./inputs', 'r') as inputs:
    inputs = [ input.strip() for input in inputs.readlines()]
    wordNb, wordLen = len(inputs), len(inputs[0])
    counts = [0] * wordLen
    for input in inputs:
        for i in range(wordLen):
            counts[i] += int(input[i])
    gamma = int(''.join([ str(count*2//wordNb) for count in counts ]), 2)
    epsilon = int(''.join([ str((count*2//wordNb+1)%2) for count in counts ]), 2)
    print(f'Gamma : {gamma}')
    print(f'Epsilon : {epsilon}')
    print(f'Power Consumption : {gamma*epsilon}')


