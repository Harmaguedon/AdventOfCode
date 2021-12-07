#! /usr/bin/python3

import numpy as np
import re

gridSize = 1000
with open('./inputs', 'r') as inputs:
    grid = np.zeros((gridSize, gridSize), dtype=int)
    for line in inputs.readlines():
        startY, startX, stopY, stopX = [ int(number) for number in re.match('(.*),(.*) -> (.*),(.*)', line.strip()).groups() ]
        width, heigth = abs(stopX-startX), abs(stopY-startY)
        if width == 0:
            dirY = (stopY-startY)//abs(stopY-startY)
            for posY in range(heigth+1):
                grid[startX, startY] += 1
                startY += dirY
        elif heigth == 0:
            dirX = (stopX-startX)//abs(stopX-startX)
            for posX in range(width+1):
                grid[startX, startY] += 1
                startX += dirX
        elif width == heigth:
            dirX = (stopX-startX)//abs(stopX-startX)
            dirY = (stopY-startY)//abs(stopY-startY)
            for count in range(width+1):
                grid[startX, startY] += 1
                startX += dirX
                startY += dirY
        else:
            print(f'Line can be handled : {line}')
    print(f'Answer : {(grid > 1).sum()}')
