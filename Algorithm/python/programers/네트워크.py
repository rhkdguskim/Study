# https://school.programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    parent = [i for i in range(n)]
    
    def find(v1):
        if v1 != parent[v1]:
            parent[v1] = find(parent[v1])
            return parent[v1]
        else:
            return v1
    
    def union(v1, v2):
        p1 = find(v1)
        p2 = find(v2)
        if p1 > p2:
            parent[p1] = p2
        else:
            parent[p2] = p1
            
    for i, computer in enumerate(computers):
        for j, is_connected in enumerate(computer):
            if i != j and is_connected == 1:
                p1 = find(i)
                p2 = find(j)
                if p1 != p2:
                    union(p1, p2)
                    
    for i in range(len(parent)):
        parent[i] = find(i)
    
    return len(set(parent))
