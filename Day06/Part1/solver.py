#! /usr/bin/python3    

nbDays = 80
with open('./inputs', 'r') as inputs:
    array = [ int(element) for element in inputs.readline().split(',') ]
    for i in range(nbDays):
        for i in range(len(array)):
            if array[i] == 0:
                array += [8]
                array[i] = 7
            array[i] -= 1
    print(f'After {nbDays} days, there are a total of {len(array)} fish')
    


