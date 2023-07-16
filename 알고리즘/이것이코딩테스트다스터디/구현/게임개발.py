# 게임 개발
# 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향) 부터 차례대로 갈 곳을 정한다.
# 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한칸을 전진한다.
# 만약 네 방향이 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한채로 한칸뒤로 가고 1딘계로 돌아간다
# 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.

N, M = map(int, input().split())
    
dy, dx, direction = map(int, input().split())
movepos = ['N', 'E', 'S', 'W']
movetype = [[-1,0], [0,1], [1,0], [0, -1]]
arr = [] # 맵 데이터
for i in range(M) :
    arr.append(list(map(int, input().split())))
    
counter = 0
def TurnLeft():
    global direction
    direction -= 1
    if(direction == -1) :
        direction = 3
        
def TurnBack():
    global direction
    direction += 2
    if(direction > 3) :
        direction -= 4
        
def moveChar(y, x):
    global dx, dy, counter
    dx = x
    dy = y
    arr[dy][dx] = 2
    counter += 1
    print("이동 하였습니다", y, x)
    
arr[dy][dx] = 2 # 초기 이동완료
        
while(True):
    if arr[dy + 1][dx] >= 1 and arr[dy - 1][dx] >= 1 and arr[dy][dx + 1] >= 1 and arr[dy][dx - 1] >= 1 : # 네 방향이 모두 이미 가본 칸이거나 바다로 되어있는 칸 인경우. 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는경우
        TurnBack()
        if(arr[dy + movetype[direction][0]][dx + movetype[direction][1]] == 2): # 이미 들렀던 곳인경우
            moveChar(dy + movetype[direction][0], dx + movetype[direction][1])
        else : # 바다인경우
            break
    
    TurnLeft()
    if(arr[dy + movetype[direction][0]][dx + movetype[direction][1]] == 0): # arr의 현재위치 파악
        moveChar(dy + movetype[direction][0], dx + movetype[direction][1])
        
print(counter)
