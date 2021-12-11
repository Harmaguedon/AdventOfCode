#! /usr/bin/python3

def keepMax(array, index):
    arrayLen, count = len(array), 0
    for input in array:
        count += int(input[index])
    if count*2 >= arrayLen:
        return array[arrayLen-count:]
    else:
        return array[:arrayLen-count]    

def keepMin(array, index):
    arrayLen, count = len(array), 0
    for input in array:
        count += int(input[index])
    if count*2 >= arrayLen:
        return array[:arrayLen-count]
    else:
        return array[arrayLen-count:]

with open('./inputs', 'r') as inputs:
    inputs = [ input.strip() for input in inputs.readlines()]
    list.sort(inputs)
    gammaArray, epsilonArray = keepMax(inputs, 0), keepMin(inputs, 0)
    for i in range(1, len(inputs[0])):
        if len(gammaArray) > 1:
            gammaArray   = keepMax(gammaArray, i)
        if len(epsilonArray) > 1:
            epsilonArray = keepMin(epsilonArray, i)

    gamma = int(gammaArray[0], 2)
    epsilon = int(epsilonArray[0], 2)
    print(f'Gamma : {gamma}')
    print(f'Epsilon : {epsilon}')
    print(f'Power Consumption : {gamma*epsilon}')




