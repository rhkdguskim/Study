# https://www.acmicpc.net/problem/15686
from itertools import combinations
N , M = map(int, input().split()) # N은 도시의 크기 M은 최대 치킨집의 개수
house = []
chickenstore = []
for i in range(N):
    inputlist = list(map(int, input().split()))
    for j in range(len(inputlist)):
        if inputlist[j] == 1: # 집이면
            house.append([i, j]) # i는 세로, j는 가로
        if inputlist[j] == 2: # 치킨집이면
            chickenstore.append([i,j])
    
def chickendistance(house, chickenstore): # 치킨거리를 구한다.
    distance = 0
    for i,j in house:
        mindistance = int(10e9)
        for k,n in chickenstore:
            cost = abs(i-k) + abs(j-n)
            if cost < mindistance: # 현재 집에서 치킨집까지의 최소거리값을 넣는다.
                mindistance = cost

        distance += mindistance # 각집에서 치킨거리 누적합을 계산한다.
                
    return distance

chickencombi = list(combinations(chickenstore, M)) # Combinations 이용하여 최대M개의 치킨집 조합을 생성한다.

minresult = int(10e9) # 최소값을 넣기위한 10e9값 초기화
for chicken in chickencombi: # 각각의 조합의 치킨거리를 구하여 최소값을 출력한다.
    cost = chickendistance(house, chicken)
    if cost < minresult:
        minresult = cost
        
print(minresult)