#! /usr/bin/python3    

def nbCommonChar(str1, str2):
    count = 0
    for char in str1:
        if char in str2:
            count += 1
    return(count)

with open('./inputs', 'r') as inputs:
    sum = 0
    for line in inputs.readlines():
        left, right = [[ ''.join(sorted(word)) for word in array ] for array in [ array.strip().split() for array in line.split('|') ] ]
        wordToNum, numToWord = {}, {}
        for word in left:
            lenWord = len(word)
            if lenWord == 2:
                wordToNum[word], numToWord[1] = 1, word
            elif lenWord == 3:
                wordToNum[word], numToWord[7] = 7, word
            elif lenWord == 4:
                wordToNum[word], numToWord[4] = 4, word
            elif lenWord == 7:
                wordToNum[word], numToWord[8] = 8, word
        for word in left:
            lenWord = len(word)
            if lenWord == 5:
                if nbCommonChar(numToWord[1], word) == 2:
                    wordToNum[word], numToWord[3] = 3, word
                elif nbCommonChar(numToWord[4], word) == 3:
                    wordToNum[word], numToWord[5] = 5, word
                else:
                    wordToNum[word], numToWord[2] = 2, word
            elif lenWord == 6:
                if nbCommonChar(numToWord[7], word) == 2:
                    wordToNum[word], numToWord[6] = 6, word
                elif nbCommonChar(numToWord[4], word) == 4:
                    wordToNum[word], numToWord[9] = 9, word
                else:
                    wordToNum[word], numToWord[0] = 0, word
        number = 0
        for word in right:
            number = number*10 + wordToNum[word]
        sum += number
    print(sum)