# https://www.acmicpc.net/problem/11000
# 1) 수업시간표를 수업시작 시간으로 정렬한다.
# 2) 하나하나 뽑아가며 room을 만들고 room에 수업시간을 이어 붙일 수 있다면 붙히고 못붙힌다면 새로운 room을 만든다.
# 여기서 room 은 강의실을 뜻한다.
from collections import deque
import sys
N = int(input())

educlass = []
for _ in range(N):
    s , t = map(int, sys.stdin.readline().split())
    educlass.append([s , t])

rooms = []
start, end = educlass.pop()
rooms.append(deque([[start, end]])) # 한개를 빼서 room을 만든다.
while educlass:
    start, end = educlass.pop()  # 첫 번째 인덱스부터 하나씩 뽑는다.
    maderoom = False
    for i in range(len(rooms)):
        if rooms[i][-1][1] <= start: # 맨 끝에있는 수업이 끝나는 시간과 비교한다.
            maderoom = True
            rooms[i].append([start, end])
            break
        elif rooms[i][0][0] >= end:
            maderoom = True
            rooms[i].appendleft([start, end])
            break
    
    if not maderoom:
        maderoom = True
        rooms.append(deque([[start, end]]))

print(len(rooms))
