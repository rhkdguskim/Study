# https://www.acmicpc.net/problem/1149
char = ['R', 'G', 'B']
r = []
g = []
b = []

N = int(input())
for i in range(N):
    i, j, k = map(int, input().split())
    r.append(i)
    g.append(j)
    b.append(k)
    
total = 0
result = []
queue = []

def colorhouse(i, char):

    if(N > i >= 0):
        if char == 'R':
            queue.append(r[i])
        elif char == 'G':
            queue.append(g[i])
        else:
            queue.append(b[i])
        
    if len(queue) == N:
        return result.append(sum(queue))

    if(len(result) and min(result) < sum(queue)):    
        return
    
    if char == 'R': # R일때
        colorhouse(i+1,'G')
        queue.pop()
        colorhouse(i+1,'B')
        queue.pop()
        
    elif char == 'G': # G일때
        colorhouse(i+1, 'R')
        queue.pop()
        colorhouse(i+1, 'B')
        queue.pop()
        
    else: # B일때
        colorhouse(i+1, 'R')
        queue.pop()
        colorhouse(i+1, 'G')
        queue.pop()
        
colorhouse(0, "R")
queue = []
colorhouse(0, "G")
queue = []
colorhouse(0, "B")
print(min(result))