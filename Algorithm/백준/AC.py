# https://www.acmicpc.net/problem/5430
import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    cmd = str(input().strip())
    n = int(input().strip())
    
    arr = list(map(str, input().replace(']', ' ').replace('[', ' ').strip().split(',')))
    arr = deque([int(c) for c in arr if c != ''])
    
    status = 0 # right = 0, left = 1
    r_cnt = 0
    error = False
    for c in cmd:
        if c == 'R': # R인경우
            r_cnt += 1
            if status == 0:
                status = 1
            else:
                status = 0
        else: # D인경우
            if len(arr) > 0:
                if status:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                error = True
                break
            
    if error:
        print("error")
    else:    
        if r_cnt % 2 == 1:
            arr.reverse()    
        print('[', end='')
        for i in range(len(arr)):
            if i == len(arr) -1:
                print(arr[i], end = '')
            else:
                print(arr[i], end = ',')
        print(']', end='')
        print()
            
    