#https://www.acmicpc.net/problem/1043
# 1. Set자료구조를 생성한다 (진실을 알게될 사람들의 집합) 파티를 한번 돈다.
# 2. 파티를 두번째 도는데 진실을 알게될 사람이 없다면 거짓말을 해도되니 카운트

N, M = map(int, input().split()) # 사람의 수, 파티의 수
graph = list(map(int, input().split())) # 진실을 아는 사람들의 리스트

truthPeopleCount = graph[0]  # 진실을 아는 사람들의 수
truthPeopleList = set()  # 진실을 아는 사람들의 리스트
if graph[1:]:
    for people in graph[1:]:
        truthPeopleList.add(people)
        
party = []
partyList = []
for _ in range(M):
    party = list(map(int ,input().split()))
    partyList.append(party[1:])
    
    
    
for party in partyList:
    for people in party:
        if people in list(truthPeopleList): # 파티에 참가하는 인원중에 진실을 아는 사람이 있다면 모든 파티원을 진실을 아는 사람들로 추가한다.
            truthPeopleList = truthPeopleList.union(party)

    
counter = 0
for party in partyList:
    flag = False
    for people in party:
        if people in list(truthPeopleList): # 파티에 참가하는 인원중에 진실을 아는 사람이 있다면 모든 파티원을 진실을 아는 사람들로 추가한다.
            flag = True
            break
    if not flag:
        counter += 1
        
print(counter)
            