#! /usr/bin/python3

with open('./inputs', 'r') as inputs:
    inputs = [ input.strip().split() for input in inputs.readlines()]
    for i in range(len(inputs)):
        inputs[i][1] = int(inputs[i][1])
    posX, posY, aim = 0, 0, 0
    for move in inputs:
        if move[0] == "forward":
            posX += move[1]
            posY += aim * move[1]
        elif move[0] == "down":
            aim += move[1]
        elif move[0] == "up":
            aim -= move[1]
        else:
            panic(f'Move unknown : {move[0]}')
    print(f'x:{posX}')
    print(f'y:{posY}')
    print(f'x*y:{posX*posY}')

