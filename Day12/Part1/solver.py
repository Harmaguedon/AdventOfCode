#! /usr/bin/python3  

import copy  

def nbPath(curPoint, seen, paths):
    if curPoint == 'end':
        return 1
    else:
        if curPoint.islower():
            seen.append(curPoint)
        sum = 0
        for nextPoint in paths[curPoint]:
            if not nextPoint in seen:
                sum += nbPath(nextPoint, copy.copy(seen), paths)
        return sum

with open('./inputs', 'r') as inputs:
    paths = {}
    for line in inputs.readlines():
        pathFrom, pathTo = line.strip().split('-')
        if pathFrom in paths.keys():
            paths[pathFrom] += [pathTo]
        else:
            paths[pathFrom] = [pathTo]
        if pathTo in paths.keys():
            paths[pathTo] += [pathFrom]
        else:
            paths[pathTo] = [pathFrom]
    print(nbPath('start', [], paths))

