# https://www.acmicpc.net/problem/2143

# A의 배열을 이중 순회하며 부분배열을 만든다. ( 누적합 )
# B 배열에서 부분배열중에 누적합과 더해서 T가 되는경우를 찾아야한다.
import sys
import bisect
input = sys.stdin.readline

T = int(input())
n = int(input())

A = [0]*n


for i, a in enumerate(list(map(int, input().split()))):
    if i == 0:
        A[i] = a
    else:
        A[i] = A[i-1] + a
    
m = int(input())
B = [0]*m

def prefix_sum(arr, s, e):
    if s > 0:
        return arr[e] - arr[s-1]
    else:
        return arr[e]

for i, b in enumerate(list(map(int, input().split()))):
    if i == 0:
        B[i] = b
    else:
        B[i] = B[i-1] + b

new_A = []
new_B = []

for i in range(n):
    for j in range(i, n):
        new_A.append((prefix_sum(A, i, j)))

for i in range(m):
    for j in range(i, m):
        new_B.append((prefix_sum(B, i, j)))
        
new_B.sort()

cnt = 0
for num in new_A:
    left = bisect.bisect_left(new_B, T - num)
    right = bisect.bisect_right(new_B, T - num)
    cnt += right - left

print(cnt)