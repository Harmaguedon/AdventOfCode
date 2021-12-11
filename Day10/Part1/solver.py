#! /usr/bin/python3    

totalErrorScore = 0
matchingChar = {'(':')', '{':'}', '[':']', '<':'>'}
score = {')':3, ']':57, '}':1197, '>':25137}
with open('./inputs', 'r') as inputs:
    for line in inputs.readlines():
        stack = []
        for char in line.strip():
            if char in matchingChar.keys():
                stack.append(char)
            elif char != matchingChar[stack.pop()]:
                totalErrorScore += score[char]
                break
print(totalErrorScore)
