# https://www.acmicpc.net/problem/17140
import sys
from collections import defaultdict
input = sys.stdin.readline

r, c, k = map(int, input().split())
A = []

for _ in range(3):
    A.append((list(map(int, input().split()))))

def get_arr_size(A):
    return len(A), len(A[0])

def R(A):
    new_A = []
    max_length = 0
    for i in range(len(A)):
        new_arr = []
        temp = defaultdict(int)
        for j in range(len(A[i])):
            if A[i][j]:
                temp[A[i][j]] += 1
        
        for key in temp:
            new_arr.append((temp[key], key))
        
        new_A.append([])
        new_arr.sort(key=lambda x:(x[0], x[1]))
        for t1, t2 in new_arr:
            new_A[i].append(t2)
            new_A[i].append(t1)
            
        max_length = max(max_length, len(new_A[i]))
    
    for arr in new_A:
        while max_length > len(arr):
            arr.append(0)
    
    return new_A

def C(A):
    new_temp = []
    max_length = 0
    for j in range(len(A[0])):
        new_arr = []
        temp = defaultdict(int)
        for i in range(len(A)):
            if A[i][j]:
                temp[A[i][j]] += 1
        
        for key in temp:
            new_arr.append((temp[key], key))
            
        new_arr.sort(key=lambda x:(x[0], x[1]))
        new_temp.append([])
        for t1, t2 in new_arr:
            new_temp[j].append(t2)
            new_temp[j].append(t1)
        max_length = max(max_length, len(new_temp[j]))
        
    new_A = [[0 for _ in range(len(new_temp))] for _ in range(max_length)]
    for i in range(len(new_temp)):
        for j in range(len(new_temp[i])):
            new_A[j][i] = new_temp[i][j]
    
    return new_A

time = 0
for _ in range(101):
    height, width = get_arr_size(A)
    if height >= r and width >= c:
        if A[r-1][c-1] == k:
            break

    if height >= width:
        A = R(A)
    else:
        A = C(A)
    time += 1

if time == 101:
    print(-1)
else:
    print(time)