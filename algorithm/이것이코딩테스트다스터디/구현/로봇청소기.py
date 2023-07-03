# https://www.acmicpc.net/problem/14503
N, M = map(int, input().split())
direction = [0, 1, 2, 3] # 북 동 남 서 현재 방향
moveback = [[1,0], [0,-1], [-1,0], [0,1]]
movefront = [[-1,0], [0,1], [1,0], [0,-1]]
room = []
robot = list()
robotdirection = 0

for _ in range(1):
    i,j,k = map(int, input().split())
    robot.append(i)
    robot.append(j)
    robotdirection = k

for _ in range(N):
    room.append(list(map(int, input().split())))

cleaned = [[False for _ in range(M)] for _ in range(N)]
counter = 0
def robotCleaner(i,j, status):
    global counter
    if not (N > i >=0 and M > j >= 0) :
        return
    
    if not cleaned[i][j]:
        cleaned[i][j] = True
        counter+=1 # 청소한 방 개수 카운트

    if checkCleanRoom(i+1,j) and checkCleanRoom(i-1,j) and checkCleanRoom(i,j+1) and checkCleanRoom(i,j-1): # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
        for k in range(len(direction)):
            if direction[k] == status:
                di, dj = moveback[k]
                if checkWall(di+i, dj+j): # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
                    return
                else: # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
                    robotCleaner(di+i, dj+j, status) 
    else: # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
        cur = Rotate(status) # 반시계 방향으로 90도 회전한다.
        di, dj = movefront[direction.index(cur)]
        if not checkCleanRoom(di+i, dj+j):
            robotCleaner(di+i, dj+j, cur) # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다. 1번으로 돌아간다.
        else:
            robotCleaner(i,j, cur) # 그렇지 않은경우 전진하지않고 1번으로 돌아간다.
        
def Rotate(status):
    cur = direction.index(status)
    if 0 > cur-1:
        return direction[3]
    else:
        return direction[cur-1]
        

def checkWall(i,j):
    if N > i >=0 and M > j >= 0:
        if room[i][j] == 1:
            return True
        else :
            return False
    else:
        return True
    
def checkCleanRoom(i,j):
    if N > i >=0 and M > j >= 0 and room[i][j] == 0 and not cleaned[i][j]:
        return False
    else :
        return True
    
robotCleaner(robot[0], robot[1], robotdirection)

print(counter)