# https://www.acmicpc.net/problem/1517
import sys
input = sys.stdin.readline

N = int(input())

data = list(map(int, input().split()))

def merge(left, right):
    global ans
    l, r = 0, 0
    temp = []
    while l < len(left) and r < len(right):
        if left[l] > right[r]:
            temp.append(right[r])
            r += 1
            ans += len(left) - l
        else:
            temp.append(left[l])
            l += 1
    
    if l == len(left):
        temp.extend(right[r:])
    else:
        temp.extend(left[l:])
    
    return temp

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

ans = 0
merge_sort(data)
print(ans)