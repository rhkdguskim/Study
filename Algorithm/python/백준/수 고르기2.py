import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

arr.sort()
left = 0; right = 1
ans = sys.maxsize

while right != len(arr) and left != len(arr):
    tmp = arr[right] - arr[left]
    if tmp >= M:
        if ans > tmp:
            ans = tmp
        left += 1
    else:
        right += 1

print(ans)