#! /usr/bin/python3    

with open('./inputs', 'r') as inputs:
    positions = sorted([ int(position) for position in inputs.readline().split(',') ])

    bestCentralPosition, bestFuel = 0, len(positions)**3
    for centralPosition in range(positions[0], positions[-1]+1):
        fuel = sum([ (abs(centralPosition - position))*(1+abs(centralPosition - position))//2 for position in positions ])
        if fuel < bestFuel:
            bestFuel = fuel
            bestCentralPosition = centralPosition
    print(f'There is a need of {bestFuel} fuel to go to the position {bestCentralPosition}')
