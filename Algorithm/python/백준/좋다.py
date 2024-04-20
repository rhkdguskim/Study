# https://www.acmicpc.net/problem/1253
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

candidate = set(arr)

ans = set()

for i in range(N):
    for j in range(N):
        if i != j:
            cost = arr[i] + arr[j]
            if arr[i] == arr[j]:
                continue
            
            if cost in candidate:
                ans.add(cost)
    
count = 0            
for num in ans:
    count += arr.count(num)
    
print(count)