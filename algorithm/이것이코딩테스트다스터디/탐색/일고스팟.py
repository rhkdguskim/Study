# https://www.acmicpc.net/problem/1261
from collections import deque

M, N = map(int, input().split()) # M 가로의 크기, N 세로의 크기
arr = []
for i in range(N): # 세로의 길이만큼 배열추가
    arr.append(list(map(int, input())))
    
def appendQueue(queue, y,x, data):
    if(M > x >=0 and N > y >= 0):
        arr[y][x] += data 
        queue.append([y,x])
    
def bfs(arr, x,y):
    queue = deque()
    queue.append([y,x])
    mindata = 0
    while queue:
        i,j = queue.popleft()
        appendQueue(queue, i+1,j, mindata)
        appendQueue(queue, i-1,j, mindata)
        appendQueue(queue, i,j-1, mindata)
        appendQueue(queue, i,j+1, mindata)
        
def bfs2(arr, x , y):
    queue = deque()
    queue.append([y,x])
    while queue:
        i,j = queue.popleft()
    
        
bfs(arr, 0, 0)
print(arr)