# https://www.acmicpc.net/problem/13164
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

arr = list(map(int, input().split()))

temp = []
for i in range(N):
    temp.append((arr[i], i))
    
temp.sort()

diff = []
for i in range(1, N):
    diff.append(temp[i][0] - temp[i-1][0])
    
diff.sort()

for _ in range(K-1):
    diff.pop()

print(sum(diff))