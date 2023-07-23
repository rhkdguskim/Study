# https://www.acmicpc.net/problem/19942
# 다이나믹 프로그래밍
from copy import deepcopy
N = int(input())
mp, mf, ms, mv = map(int, input().split()) # 단,지,탄,비
table = [[0, 0, 0, 0]]
for _ in range(N):
    table.append(list(map(int, input().split()))) # 단,지,탄,비, 가격


minvalue = 2001 # 최소값 두는 문제가 있음.
minqueue = []
def diet(nut, cost, depth, queue): # depth 네이밍룰 idx
    global minvalue
    global minqueue
    if cost > minvalue: # 백트래킹 조건
        return 2001
    
    if nut[0] >= mp and nut[1] >= mf and nut[2] >= ms and nut[3] >= mv: # 최소값 초기화
        if minvalue > cost:
            minqueue = queue
            minvalue = cost
        return minvalue
    
    if depth == N+1:
        return 2001

    newnut = deepcopy(nut)
    newqueue = deepcopy(queue)
    newcost = cost + table[depth][4]
    newqueue.append(depth)
    
    for i in range(4):
        newnut[i] += table[depth][i]
    
    # 해당 아이템을 현재 반영한경우와 반영하지 않은 경우 모두 탐색
    result = min(diet(newnut, newcost, depth+1, newqueue), diet(nut, cost, depth+1, queue))
    
    return result

nut = [0, 0, 0, 0]
queue = []
diet(nut, 0, 1, queue)

if minvalue == 2001:
    print(-1)
else:
    print(minvalue)
    print(*minqueue)