#! /usr/bin/python3    

nbDays = 256
with open('./inputs', 'r') as inputs:
    nbNewFish = [0]*9
    for element in inputs.readline().split(','):
        nbNewFish[int(element)] += 1
    for i in range(nbDays):
        nbNewFish = [nbNewFish[1], nbNewFish[2], nbNewFish[3], nbNewFish[4], nbNewFish[5], nbNewFish[6], nbNewFish[7]+nbNewFish[0], nbNewFish[8], nbNewFish[0]]
    print(f'After {nbDays} days, there are a total of {sum(nbNewFish)} fish')
    


