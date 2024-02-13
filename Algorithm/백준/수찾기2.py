import sys
input = sys.stdin.readline

N = int(input())
num = set(list(map(int, input().split())))

M = int(input())
queries = list(map(int, input().split()))

for query in queries:
    if query in num:
        print(1)
    else:
        print(0)