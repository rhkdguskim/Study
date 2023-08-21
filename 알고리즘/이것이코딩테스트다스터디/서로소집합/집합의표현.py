#https://www.acmicpc.net/problem/1717
import sys
sys.setrecursionlimit(10**6)
n,m = map(int, input().split())
input = sys.stdin.readline

parent =[i for i in range(n+1)] # 0부터 N개의 집합을 만들고 부모노드를 가르키는 배열을 만든다.


def union(a,b):
   v1 = getParent(a)
   v2 = getParent(b)
   if v1 > v2: # 값이 큰 값이 작은값의 부모로 들어간다.
       parent[v1] = v2
   else:
       parent[v2] = v1
       
def getParent(a):
    if a != parent[a]:
        parent[a] = getParent(parent[a])
        
    return parent[a]


for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0: # 0이면 합집합 연산을 수행한다.
        if a != b:
            union(a,b)
    else:
        v1 = getParent(a)
        v2 = getParent(b)
        if v1 != v2: # 부모가 다른경우 공통집합이 아니다.
            print("NO")
        else:
            print("YES")