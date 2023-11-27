# https://www.acmicpc.net/problem/1039
import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

N, K = map(int, input().strip().split())

number = list(str(N))

visited = set()

queue = deque()
queue.append((number, 0))
ans = -1
while queue:
    number, cost = queue.popleft()
    
    if cost == K:
        ans = max(ans, int(''.join(number[n] for n in range(len(number)))))
        continue
    
    for i in range(len(number)):
        for j in range(i+1, len(number)):
            temp = deepcopy(number)
            temp[i], temp[j] = temp[j], temp[i]
            
            tempnumber = ''.join(temp[n] for n in range(len(temp)))
            
            # 문제의 조건 첫자리가 0인경우와 이미 방문한 경우
            if temp[0] == '0' or (tempnumber, cost+1) in visited:
                continue
            
            # 이미 방문횟수가 넘은경우
            if cost >= K:
                continue
                
            visited.add((tempnumber, cost + 1))
            queue.append((temp, cost + 1))

print(ans)
#print(visited)