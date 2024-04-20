# https://www.acmicpc.net/problem/8983
import sys
input = sys.stdin.readline

M, N, L = map(int, input().split())

attack = list(map(int, input().split()))
animal = list(map(int, input().split()) for _ in range(N))
attack.sort()

ans = 0
for x, y in animal:
    if (y>L):
        continue
    
    s = x+y-L
    e = x-y+L
    start, end = 0, M-1
    while start <= end:
        mid = (start+end)//2
        if attack[mid] >= s and attack[mid] <= e:
            ans += 1
            break
        elif attack[mid] < e:
            start = mid + 1
        else:
            end = mid - 1
print(ans)