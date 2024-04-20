#https://www.acmicpc.net/problem/20055
from collections import deque

N, K = map(int, input().split())
zerocount = 0
def rotate(table, robotvisited):
    num = table.pop()
    table.appendleft(num)
    visited = robotvisited.pop()
    robotvisited.appendleft(visited)
    
def moverobot(table, robotvisited):
    global zerocount
    for i in range(N-1, -1, -1):
        if table[i+1] > 0 and not robotvisited[i+1] and robotvisited[i]:
            robotvisited[i] = False
            table[i+1] -= 1
            robotvisited[i + 1] = True
            if table[i+1] == 0:
                zerocount += 1
                
def pushRobot(table, robotvisited):
    global zerocount
    if table[0] > 0: # 내구성이 존재한다면
        robotvisited[0] = True
        table[0] -= 1
        if table[0] == 0:
            zerocount += 1

def popRobot(robotvisited):
    if robotvisited[N - 1]:
        robotvisited[N - 1] = False
    
def vailate(table):
    global zerocount
    if zerocount >= K:
        return False
    else:
        return True

table = deque(map(int, input().split())) # 컨베이어벨트
robotvisited = deque(False for _ in range(len(table))) # 로봇이 있는지 없는지 확인

answer = 0
while vailate(table):
    
    answer += 1
    rotate(table, robotvisited)
    popRobot(robotvisited)
    moverobot(table, robotvisited)
    popRobot(robotvisited)
    pushRobot(table, robotvisited)
    
print(answer)