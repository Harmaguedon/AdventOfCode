#! /usr/bin/python3    

autocompleteScores = []
matchingChar = {'(':')', '{':'}', '[':']', '<':'>'}
score = {')':1, ']':2, '}':3, '>':4}
with open('./inputs', 'r') as inputs:
    for line in inputs.readlines():
        stack = []
        for char in line.strip():
            if char in matchingChar.keys():
                stack.append(char)
            elif char != matchingChar[stack.pop()]:
                stack = []
                break
        if len(stack) != 0:
            autocompleteScore = 0
            while len(stack) != 0:
                autocompleteScore = autocompleteScore * 5 + score[matchingChar[stack.pop()]]
            autocompleteScores.append(autocompleteScore)
print(sorted(autocompleteScores)[len(autocompleteScores)//2])
