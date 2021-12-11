#! /usr/bin/python3    

import numpy as np

def flash(grid):
    pos = np.argwhere(grid == 10)
    if len(pos) > 0:
        for x in range(max(0,pos[0][0]-1), min(9,pos[0][0]+1)+1):
            for y in range(max(0,pos[0][1]-1), min(9,pos[0][1]+1)+1):
                if grid[x][y] <= 9:
                    grid[x][y] += 1
        grid[pos[0][0]][pos[0][1]] = 11
        return True
    return False

nbFlash = 0
nbTurns = 100
grid = np.zeros((10,10), dtype=int)
with open('./inputs', 'r') as inputs:
    for index, line in enumerate(inputs.readlines()):
        grid[index] = np.array(list(line.strip()))
    for i in range(nbTurns):
        grid += 1
        while flash(grid):
            nbFlash += 1
        for posX, posY in np.argwhere(grid == 11):
            grid[posX][posY] = 0
print(nbFlash)
