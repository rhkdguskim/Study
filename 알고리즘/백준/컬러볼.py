# https://www.acmicpc.net/problem/10800
# 컬러별로 사이즈를 담고 정렬한다.
# 구간합을 초기화한다. ( 펜윅 트리 ) logn
# 자기자신보다 작은 값을 찾는다. ( 이분탐색한다) logn
# 구간합을 구한다.

import sys
input = sys.stdin.readline

N = int(input())
player = []
colortable = [0 for _ in range(N+1)]
numbertable = [0 for _ in range(2001)]
for i in range(1, N+1):
    color, size = map(int, input().split())
    player.append((color, size, i))

player.sort(key=lambda x: (x[1], x[0]))

acc = 0
result = [0 for _ in range(N+1)]
prev_color, prev_size, prev_sum = 0, 0, 0
for color, size, idx in player:
    if color == prev_color and prev_size == size:
        result[idx] = prev_sum
    else:
        result[idx] = acc - colortable[color] - numbertable[size]
        
    colortable[color] += size
    numbertable[size] += size
    prev_color, prev_size = color, size
    prev_sum = result[idx]
    acc += size
    
for i in range(1, N+1):
    print(result[i])