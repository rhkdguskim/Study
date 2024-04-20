# https://www.acmicpc.net/problem/2585
# 해당 문제는 이분탐색 + 그래프 문제이다.
# 이진 탐색의 mid 값을 기름통으로 정한다.
# 너비우선탐색으로 갈 수 있는 최소 거리를 구한다.
# 최소거리를 구하면 원하는 k값과 비교를 하여 값이 작을경우 
# 기름통 크기를 좁히고 k값 보다 클경우 기름통의 크기를 키운다.
import sys
import math
from collections import deque

def input(): return sys.stdin.readline().rstrip()

def getDistance(x1,y1, x2, y2):
    return int(math.sqrt(math.pow(abs(x1-x2),2) + math.pow(abs(y1-y2),2)))

def getTankSize(distance):
    tank = distance//10
    if distance % 10 != 0:
        tank += 1
    return tank

def GetCango(tanksize):
    visited = [False for _ in range(len(arrival))]
    queue = deque()
    queue.append([0,0,0]) #자기자신
    visited[0] = True
    result = 0
    while queue:
        x,y, count = queue.popleft()
        if x == 10000 and y == 10000:
            return True
        
        if count > k:
            continue
        
        for i in range(len(arrival)):
            if count <= k:
                if tanksize >= getTankSize(getDistance(x, y, arrival[i][0], arrival[i][1])) and not visited[i]:
                    visited[i] = True
                    queue.append([arrival[i][0], arrival[i][1], count+1])
    
    return False
        
    

distance = getDistance(0,0,10000,10000)
tank = getTankSize(distance)

start = 1
end = tank

n, k = map(int, input().split())

arrival = []
arrival.append([0,0])
for _ in range(n):
    arrival.append(list(map(int, input().split())))

arrival.append([10000,10000])
minresult = 1000
while start <= end:
    mid = (start + end) // 2 # 기름통크기
    # 최소 cango를 를 구해야함. ( 탐색문제로 다시 풀어야함)
    
    #print(mid, cango)
    if GetCango(mid): # 급유횟수가 클경우, 기름통을 늘린다.
        minresult = mid
        end = mid - 1
    else: # 급유횟수가 작을경우, 기름통을 줄인다.
        start = mid + 1
        
print(minresult)