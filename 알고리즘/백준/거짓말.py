# https://www.acmicpc.net/problem/1043
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split()) # 사람의 수, 파티의 수
person = [set() for _ in range(N+1)] # 해당 사림이 파티에 같이 참여했던 사람들
temp = list(map(int, input().split()))
truth_people = set()
if temp[0] > 0:
    for p in temp[1:]:
        truth_people.add(p)

partys = []
for _ in range(M):
    temp2 =  list(map(int, input().split()))
    
    # 자기자신이 파티에 참여했던 사람들의 집합
    for p in temp2[1:]:
        for p2 in temp2[1:]:
            if p != p2:
                person[p].add(p2)
    
    partys.append(temp2[1:])
    
    
queue = deque([p for p in truth_people])
visited = [False for _ in range(N+1)]
# 진실을 아는 사람이 단 한명이라도 존재한다면 이 사람때문에 파티에 참석했던 사람들 모두 다 진실을 알면 안되는 사람이 된다.
while queue: 
    p = queue.popleft()
    for new_p in person[p]:
        if not visited[new_p]:
            visited[new_p] = True
            truth_people.add(new_p)
            queue.append(new_p)

ans = M
for party in partys:
    flag = False
    for p_p in party:
        if p_p in truth_people: # 파티에 진실을 아는 사람이 단 한명이라도 존재한다면
            flag = True
            break
        
    if flag:
        ans -=1 
        
print(ans)