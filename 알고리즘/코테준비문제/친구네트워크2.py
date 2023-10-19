import sys
input = sys.stdin.readline

def find(name):
    if parent[name] == name:
        return parent[name]
    else:
        parent[name] = find(parent[name])
        return parent[name]

def union(name1, name2):
    p1 = find(name1)
    p2 = find(name2)

    if p1 == p2:
        return

    parentset[p1] = parentset[p1].union(parentset[p2])
    parent[p2] = p1

T = int(input())
for _ in range(T):
    N = int(input())
    parent = dict()
    parentset = dict()
    for _ in range(N):
        a, b = map(str, input().split())
        if a not in parent:
            parent[a] = a
            parentset[a] = set()
            parentset[a].add(a)
        if b not in parent:
            parent[b] = b
            parentset[b] = set()
            parentset[b].add(b)

        union(a, b)
        p = find(a)
        print(len(parentset[p]))
