# 1. 현재위치에서 갈 수 있는 모든 경로를 구한다. (가지고있는 맥주의 개수와 거리 계산)
# 2. 목적지가 페스티벌이면 종료한다 (Happy를 출력), 목적지가편의점이면 에너지를 충전하고 현재위치에서 갈 수 있는 모든 경로를 구한다(단, 이미 방문했던 위치는 다시 재방문 해서는 안됨.)
# 3. 1와 2를 반복하고 모든 경로를 다 방문했는데도 페스티벌에 도착 못했다면 Sad를 출력

# dfs 로 문제를 접근하면 안됬었음.
# destnation가 계속 반복적으로 실행된다. 깊이우선탐색, 너비우선탐색 둘중 뭘로 탐색해야할까?
# 탐색을 고르는 과정의 학습이 필요하다

# 너비우선탐색으로 진행한다.
# 깊이우선, 너비우선탐색 (너비우선탐색 : 최단거리에 좋다.) (깊이우선탐색 : 추가적인 학습이 필요할겉음 감을 못잡겠음.)
# 
import sys
from collections import deque
input = sys.stdin.readline
t = int(input()) # 테스트 케이스 개수     

            
for _ in range(t):
    n = int(input()) # 편의점 개수
    house = list(map(int, input().split())) # house[0] x좌표 house[1] y좌표
    destnation = []
    festival = [] # 페스티벌 좌표 festival[0] x좌표, festival[1] y좌표 festival[2]는 도착idx
    

    destnation.append([house[0], house[1], 0])
    for i in range(n+1):
        dest = list(map(int, input().split()))
        dest.append(i+1)
        if i == n:
            festival = dest
        destnation.append(dest) # 모든 경로를 지정한다.
    finishedFlag = False
    

    visited = [False for _ in range(n+2)] # 도착 여부를 체크하는 리스트
    
    queue = deque()
    queue.append([house[0], house[1], 0])
    visited[0] = True
    while queue:
        newx, newy, index = queue.popleft()
        
        if index == festival[2]:
            finishedFlag = True
            break
        
        for dest in destnation: # 여기서 
            x,y, idx = dest
            if 1000 >= abs(x-newx) + abs(y-newy) and not visited[idx]: # 맥주 20개 x 50미터 갈 수있음. 거리가 1000 이상인 목적지와 방문하지 않는 목적지만 탐색한다.
                queue.append([x,y,idx])
                visited[idx] = True
    
    if finishedFlag :
        print("happy")
    else:
        print("sad")
        


        
