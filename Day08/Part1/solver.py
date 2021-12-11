#! /usr/bin/python3    

with open('./inputs', 'r') as inputs:
    nb1478 = 0
    for words in [ line.split('|')[1].strip().split() for line in inputs.readlines( )]:
        for word in words:
            lenWord = len(word)
            if lenWord == 2 or lenWord == 3 or lenWord == 4 or lenWord == 7:
                nb1478 += 1
    print(nb1478)
