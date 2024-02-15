# https://www.acmicpc.net/problem/13334
import sys
input = sys.stdin.readline

n = int(input())

road = []
for _ in range(n):
    road.append((sorted(list(map(int, input().split())))))
    
road.sort(key=lambda x:x[0])

d = int(input())

start = road[0][0]
end = road[-1][1]
ans = 0
while end >= start:
    mid = (start+end)//2
    x1, x2 = mid, mid + d
    count, left, right = 0, 0, 0
    for s, e in road:
        if x1 <= s and e <= x2:
            count += 1
        elif s < x1 and e < x2:
            left += 1
        elif s > x1 and e > x2:
            right += 1
        else:
            if abs(x1 - s) >= abs(e - x2):
                left += 1
            else:
                right += 1
            
    ans = max(count, ans)
    if left >= right:
        end = mid - 1
    else:
        start = mid + 1

print(ans)