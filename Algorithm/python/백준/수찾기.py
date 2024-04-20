# https://www.acmicpc.net/problem/1920
import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))

M = int(input())
queries = list(map(int, input().split()))

# 숫자를 정렬한다 O(Nlog(N))
num.sort()

def find_num(arr, query):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == query:
            return 1
        elif arr[mid] > query:
            end = mid - 1
        else:
            start = mid + 1
    
    return 0
    
for query in queries:
    print(find_num(num, query))
    
