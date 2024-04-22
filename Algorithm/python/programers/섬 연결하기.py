# n개의 섬 사이에 다리를 건설하는 비용 costs가 주어질때
# 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return 하라
# 최소신장트리!!

def find(a, parent):
    if a != parent[a]:
        parent[a] = find(parent[a], parent)
        return parent[a]
    else:
        return a

def union(a, b, parent):
    p1 = find(a, parent)
    p2 = find(b, parent)

    if p1 > p2:
        parent[p1] = p2
    else:
        parent[p2] = p1

def solution(n, costs):
    # 다리를 가장 짧은 순으로 정렬
    costs.sort(key=lambda x:x[2])

    parent = [i for i in range(n+1)]

    answer = 0

    for a, b, d in costs:
        p1 = find(a, parent)
        p2 = find(b, parent)
        if p1 != p2:
            union(p1, p2, parent)
            answer += d

    return answer