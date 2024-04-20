#https://www.acmicpc.net/problem/1043
# 1. Set자료구조를 생성한다 (진실을 알게될 사람들의 집합) 파티를 한번 돈다.
# 2. 파티를 두번째 도는데 진실을 알게될 사람이 없다면 거짓말을 해도되니 카운트
N, M = map(int, input().split()) 
graph = list(map(int, input().split()))

truthPeopleCount = graph[0]
truthPeopleList = set(graph[1:])

partyList = [list(map(int, input().split()))[1:] for _ in range(M)]

updated = True
while updated:
    updated = False
    for party in partyList:
        if any(person in truthPeopleList for person in party):
            if not truthPeopleList.issuperset(party): # 새로운 사람을 추가하는지 확인
                truthPeopleList = truthPeopleList.union(party)
                updated = True

counter = sum(1 for party in partyList if not any(person in truthPeopleList for person in party))
print(counter)