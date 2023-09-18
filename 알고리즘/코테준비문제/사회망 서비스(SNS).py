# https://www.acmicpc.net/problem/2533
# 내가 얼리어뎁터이면 친구들은 얼리어뎁터가 아니다.
# 내가 얼리어뎁터가 아니라면 친구들이 얼리어뎁터이어야한다.
# 위의 조건으로 재귀를 통하여 문제를 해결한다.
# 재귀 끝나는 조건은 모든 친구들을 방문 했을때이다. 즉 카운터가 1000000일때이다.
# 카운터에 다 도달했을때 얼리어답터의 숫자를 샌다.
# 다음계산할때 최소얼리어뎁터의 개수보다 현재 얼리어뎁터의 숫자가 큰경우 종료한다. (탐색 필요 없음)


N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b  = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

minresult = 1000001 # 모든 사람이 얼리어뎁터인경우가 최대값
earlyadaptors = [-1 for _ in range(N+1)]
def earlyadaptor(node, bEarly, Earlyadators, visitedCount):
    global minresult
    visitedCount += 1
    if bEarly:
        earlyadaptors[node] = 1
        Earlyadators += 1
    else:
        earlyadaptors[node] = 0
        
    if visitedCount >= N: # 모두다방문 했을때만 최소값을 초기화 해야한다.
        minresult = Earlyadators
    
        
    if Earlyadators >= minresult:
        return
    
    for newnode in graph[node]:
        if earlyadaptors[newnode] == -1: # 최초 방문일때만 방문한다.
            if bEarly: # 자기자신이 얼리어뎁터라면 친구는 얼리어뎁터가 아니다.
                Earlyadators = earlyadaptor(newnode, False, Earlyadators, visitedCount)
                earlyadaptors[newnode] = -1
            else: # 자기자신이 얼리어뎁터가 아니라면 친구는 얼리어뎁터 이어야한다.
                Earlyadators = earlyadaptor(newnode, True, Earlyadators, visitedCount)
                earlyadaptors[newnode] = -1
                
            

earlyadaptor(1,False,0,0)
earlyadaptors[1] = -1

earlyadaptor(1,True,0,0)
earlyadaptors[1] = -1

print(minresult)