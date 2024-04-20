import sys
input = sys.stdin.readline

N = int(input())

advanture = list(map(int, input().split()))
advanture.sort(reverse=True)

ans = 0
cnt = 0
for af in advanture:
    if af > cnt:
        cnt += 1
    else:
        ans += 1
        cnt = 0
        
print(ans)