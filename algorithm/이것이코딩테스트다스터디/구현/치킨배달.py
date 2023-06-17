# https://www.acmicpc.net/problem/15686
from collections import deque
INF = int(10e9)
N , M = map(int, input().split()) # N은 도시의 크기 M은 최대 치킨집의 개수
house = []
chik = []
for i in range(N):
    inputlist = list(map(int, input().split()))
    for j in range(len(inputlist)):
        if(inputlist[j] == 1): # 집이면
            house.append([i, j]) # i는 세로, j는 가로
        elif(inputlist[j] == 2): #치킨집이면 :
            chik.append([i, j]) # i는 세로, j는 가로

def appendqueue(queue, distance, dis, y, x):
    if(N > y >= 0 and N > x >=0):
        cost = dis + 1
        if(distance[y][x] > cost): # 집이거나 빈거리일경우만 이동한다.
            distance[y][x] = cost
            queue.append([distance[y][x], y, x])


def bfs(i,j, distance): # 치킨집으로부터 집까지의 최단거리를 구한다.
    queue = deque()
    distance[i][j] = 0
    queue.append((distance[i][j], i, j))

    while queue :
       dis, y, x = queue.popleft()
       appendqueue(queue, distance, dis, y+1, x)
       appendqueue(queue, distance, dis, y-1, x)
       appendqueue(queue, distance, dis, y, x+1)
       appendqueue(queue, distance, dis, y, x-1)

chieckenhouse = dict(list())

result = dict()
for i in chik :
    distance = [[INF for _ in range(N)] for _ in range(N)]
    bfs(i[0], i[1], distance)
    result[str(i[0])+str(i[1])] = list()
    #print("치킨집:", i[0],i[1])
    for j in house:
        result[str(i[0])+str(i[1])].append(distance[j[0]][j[1]])
        #print("집:", j[0],j[1],"거리", distance[j[0]][j[1]]) 

citychiecken = []
for data in result:
    list = result[data]
    sum = 0
    for n in list:
        sum += n
    citychiecken.append([sum, data])
    
citychiecken.sort()

minhouse = [INF] * len(house)
for i in range(M):
    list = citychiecken[i]
    for j in range(len(house)):
        if(minhouse[j] > result[list[1]][j]):
            minhouse[j] = result[list[1]][j]
            
housesum = 0
for i in range(len(minhouse)):
    housesum += minhouse[i]


print(housesum)