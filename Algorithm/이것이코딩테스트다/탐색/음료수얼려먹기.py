# N * M 크기의 얼음 틀이 있다. 구멍이 뚤려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
# 구멍이 뚤려있는 부분끼리 상,하,좌,우로 붙어있는경우 서로 연결되어있는걸로 간주한다.
# 이때 얼음 틀의 모양이 주어졌을때 생성되는 총 아이스크림 개수를 구하는 프로그램을 작성하시오.

from collections import deque

N, M = map(int, input().split())
arr = list()
for _ in range(N) :
    arr.append(list(map(int, input())))

queue = deque()
moves = [(1,0), (-1,0), (0,1), (0,-1)] # 북, 남, 동, 서
    

visit = [[False for _ in range(M)] for _ in range(N)]
counter = 0

def dps(y, x):
    visit[y][x] = True
    
    if (N > y+1 >=0 and arr[y+1][x] == 0 and visit[y+1][x] == False): # 북쪽을 탐색
        dps(y + 1, x)
    elif (N > y-1 >=0 and arr[y-1][x] == 0 and visit[y-1][x] == False): # 남쪽을 탐색
        dps(y - 1, x)
    elif (M > x+1 >= 0 and arr[y][x+1] == 0 and visit[y][x+1] == False): # 동쪽을 탐색
        dps(y, x+1)
    elif (M > x-1 >=0 and arr[y][x-1] == 0 and visit[y][x-1] == False): # 서쪽을 탐색
        dps(y, x-1)
    else :
        print("탐색을 종료합니다.")

for y in range(N):
    for x in range(M):
        if (visit[y][x] == False and arr[y][x] == 0):
            dps(y,x)
            counter += 1
            
print(counter)
    