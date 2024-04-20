# https://www.acmicpc.net/problem/2629
'''
3
7 8 9
1
6
'''
import sys
input = sys.stdin.readline

N = int(input())
chu = list(map(int, input().split()))

M = int(input())
gu = list(map(int, input().split()))

v = [False for _ in range(40001)]

#chu.sort(reverse=True)

for c in chu:
    # 오른쪽, 왼쪽에 둘 수 있음을 표기한다.
    update = []
    for w in range(1, len(v)- c):
        if v[w]:
            update.append(w+c)
            update.append(abs(w-c))
    
    # 자기자신을 무게를 잴 수 있다고 표기한다.
    v[c] = True
    for u in update:
        v[u] = True

for g in gu:
    if v[g]:
        print('Y', end= ' ')
    else:
        print('N', end= ' ')
print()