#! /usr/bin/python3

import numpy as np

gridSize = 5
with open('./inputs', 'r') as inputs:
    numbers = [ int(number) for number in inputs.readline().strip().split(',') ]
    grids = []
    for i, row in enumerate(inputs):
        if i%(gridSize+1) == 0:
            grids += [np.zeros((gridSize, gridSize), dtype=int)]
        else:
            grids[i//(gridSize+1)][i%(gridSize+1)-1] += [int(number) for number in row.strip().split()]
    gridsFill = [[ 0 for i in range(gridSize*2) ] for i in range(len(grids)) ]
    nbFinishedGrid = 0

    for number in numbers:
        for gridIndex, grid in enumerate(grids):
            pos = np.argwhere(grid == number)
            if len(pos) > 0:
                grid[pos[0][0]][pos[0][1]] = -1
                gridsFill[gridIndex][pos[0][0]]          += 1
                gridsFill[gridIndex][pos[0][1]+gridSize] += 1
                if gridsFill[gridIndex][pos[0][0]] == gridSize or gridsFill[gridIndex][pos[0][1]+gridSize] == gridSize:
                    nbFinishedGrid += 1
                    if nbFinishedGrid != len(grids):
                        grid.fill(-1)
                    else:
                        print(f'Number => {number}')
                        print(f'Sum of unmarked numbers => {grid[grid!=-1].sum()}')
                        print(f'Answer => {grid[grid!=-1].sum()*number}')
                        exit()
                        


