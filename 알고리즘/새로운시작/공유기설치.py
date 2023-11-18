import sys
input = sys.stdin.readline

N, C = map(int, input().split())

home = []
for _ in range(N):
    home.append(int(input()))

home.sort()

start = 0
end = home[-1] + home[0] # 공유기를 놓을 수 있는 최대거리중 중간값
ans = 0
while start <= end:
    mid = (start + end) // 2

    prev = home[0]
    cnt = 1
    for i in range(1, len(home)):
        if home[i] - prev >= mid: # 공유기를 놓을 수 있다면
            prev = home[i]
            cnt += 1
            

    if cnt >= C:
        ans = max(mid, ans)
        start = mid + 1
    else:
        end = mid - 1
        
print(ans)