#! /usr/bin/python3    

with open('./inputs', 'r') as inputs:
    heightMap = []
    for line in inputs.readlines():
        heightMap += [[int(height) for height in line.strip()]]
    lowPoints = []
    width, height = len(heightMap[0]), len(heightMap)
    for x in range(height):
        for y in range(width):
            if ((x == 0 or heightMap[x][y]<heightMap[x-1][y]) and
                (x == height-1 or heightMap[x][y]<heightMap[x+1][y]) and
                (y == 0 or heightMap[x][y]<heightMap[x][y-1]) and
                (y == width-1 or heightMap[x][y]<heightMap[x][y+1])):
                lowPoints += [[x,y]]
    bassinSize = []
    for lowPoint in lowPoints:
        seen, new = [lowPoint], [lowPoint]
        while len(new) != 0:
            x, y = new[0]
            if x > 0 and heightMap[x][y]<heightMap[x-1][y]<9 and [x-1, y] not in seen:
                new  += [[x-1,y]]
                seen += [[x-1,y]]
            if x < height-1 and heightMap[x][y]<heightMap[x+1][y]<9 and [x+1, y] not in seen:
                new  += [[x+1,y]]
                seen += [[x+1,y]]
            if y > 0 and heightMap[x][y]<heightMap[x][y-1]<9 and [x, y-1] not in seen:
                new  += [[x,y-1]]
                seen += [[x,y-1]]
            if y < width-1 and heightMap[x][y]<heightMap[x][y+1]<9 and [x, y+1] not in seen:
                new  += [[x,y+1]]
                seen += [[x,y+1]]
            new = new[1:]
        bassinSize += [len(seen)]
    bassinSize.sort()
    print(f'Answer : {bassinSize[-1]*bassinSize[-2]*bassinSize[-3]}')
