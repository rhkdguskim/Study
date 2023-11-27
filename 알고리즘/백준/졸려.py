# https://www.acmicpc.net/problem/9519
import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

X = int(input())
word = list(input().strip())
temp_word = deepcopy(word)

def solve(char):
    temp = deque()
    temp2 = deque()
    for i in range(len(char)):
        if i % 2 == 1:
            temp.appendleft(char[i])
        else:
            temp2.append(char[i])
    
    return list(temp2) + list(temp)

cnt = 0
while True:
    cnt += 1
    word = solve(word)
    if temp_word == word:
        break

for _ in range(X % cnt):
    temp_word = solve(temp_word)
    
print(''.join(s for s in temp_word))