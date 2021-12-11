#! /usr/bin/python3    

with open('./inputs', 'r') as inputs:
    totalRiskLevel = 0
    heightMap = []
    for line in inputs.readlines():
        heightMap += [[int(height) for height in line.strip()]]
    width, height = len(heightMap[0]), len(heightMap)
    for x in range(height):
        for y in range(width):
            if ((x == 0 or heightMap[x][y]<heightMap[x-1][y]) and
                (x == height-1 or heightMap[x][y]<heightMap[x+1][y]) and
                (y == 0 or heightMap[x][y]<heightMap[x][y-1]) and
                (y == width-1 or heightMap[x][y]<heightMap[x][y+1])):
                totalRiskLevel += heightMap[x][y]+1
    print(totalRiskLevel)
