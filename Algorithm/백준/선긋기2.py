import sys
input = sys.stdin.readline
N = int(input().rstrip())
arr = []
for _ in range(N):
    s,e = map(int,input().rstrip().split())
    arr.append((s,e))

arr.sort(key=lambda x : (x[0]))

tot = 0
max_check = -int(1e9)

for s,e in arr:
    if s > max_check: # 선분 개시
        tot += e-s
        max_check = e

    elif s <= max_check and e > max_check:
        tot += (e-max_check)
        max_check = e

print(tot)
