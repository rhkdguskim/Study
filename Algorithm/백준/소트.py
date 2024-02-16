#https://www.acmicpc.net/problem/1083
import sys
input = sys.stdin.readline

def max_n(index):
    max_value, idx = arr[index], index
    for i in range(index + 1, min(N, index + S + 1)):
        if arr[i] > max_value:
            max_value = arr[i]
            idx = i
    return max_value, idx


N = int(input())
arr = list(map(int, input().split()))
S = int(input())

for i in range(N - 1):
    max_value, idx = max_n(i)
    if idx != i:
        arr.pop(idx)
        arr.insert(i, max_value)
        S -= (idx - i)
        
print(*arr)