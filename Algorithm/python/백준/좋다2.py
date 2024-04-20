# https://www.acmicpc.net/problem/1253
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

def find(i):
    start = 0
    end = len(arr)-1
    while end > start:
        cost = arr[start] + arr[end]
        if cost == arr[i]:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                return True
        elif cost > arr[i]:
            end -= 1
        else:
            start += 1
            
    return False

ans = 0
for i in range(len(arr)):
    if find(i):
        ans += 1
                
print(ans)