#https://www.acmicpc.net/problem/20055
from collections import deque
from copy import deepcopy
N, K = map(int, input().split())

def rotate(table, robotvisited, robot):
    num = table.pop()
    table.appendleft(num)
    visited = robotvisited.pop()
    robotvisited.appendleft(visited)
    queue = deque()
    while robot:
        idx = robot.pop()
        if idx == N-1: # 마지막위치에 있는 로봇이라면
            queue.append(0)
        else:
            queue.append(idx+1)
    
    robot = deepcopy(queue)
    
def moverobot(table, robotvisited, robot):
    queue = deque()
    while robot:
        idx = robot.pop()
        if idx == N-1: # 마지막위치에 있는 로봇이라면
            if not robotvisited[0] and table[0] > 0: # 로봇이 없고 내구도가 0이 아니라면 움직인다.
                robotvisited[idx] = False
                robotvisited[0] = True
                table[0] -= 1
                queue.append(0)
            else:
                queue.append(idx)
        else:
            if not robotvisited[idx+1] and table[idx+1] > 0: # 다음에 놓일 조건 만족
                
                robotvisited[idx] = False
                robotvisited[idx+1] = True
                table[idx+1] -= 1
                queue.append(idx+1)
            else:
                queue.append(idx)
                
    robot = deepcopy(queue)
                
def pushRobot(table, robotvisited, robot):
    if table[0] > 0: # 내구성이 존재한다면
        robotvisited[0] = True
        robot.append(0)
        table[0] -= 1
        
def popRobot(robotvisited, robot):
    queue = deque()
    if robotvisited[N//2 + 1]:
        robotvisited = False
    
    while robot:
        idx = robot.pop()
        if idx != ((N//2) +1):
            queue.append(idx)
            
    robot = deepcopy(queue)
        
            
    
def vailate(table):
    if table.count(0) >= K:
        return False
    else:
        return True
    


table = deque(map(int, input().split())) # 컨베이어벨트
robotvisited = deque(False for _ in range(len(table))) # 로봇이 있는지 없는지 확인
robot = deque() # 로봇큐

answer = 0
while vailate(table):
    
    answer += 1
    popRobot(robotvisited, robot)
    rotate(table, robotvisited, robot)
    moverobot(table, robotvisited, robot)
    pushRobot(table, robotvisited, robot)
    
print(answer)
    
    