#https://www.acmicpc.net/problem/4195
import sys
input = sys.stdin.readline

T = int(input())

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
        return parent[a]
    else:
        return parent[a]

def union(a, b):
    parent[b] = a
    friend[a] += friend[b]

for _ in range(T):
    F = int(input())
    friend = dict()
    parent = dict()
    for i in range(F):
        friend1, friend2 = map(str, input().split())
        
        if friend1 not in parent:
            parent[friend1] = friend1
            friend[friend1] = 1
            
        if friend2 not in parent:
            parent[friend2] = friend2
            friend[friend2] = 1
        
        v1 = find(friend1)
        v2 = find(friend2)
        
        if v1 != v2:
            union(v1, v2)
        
        print(friend[find(friend1)])

        
        