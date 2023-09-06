# https://www.acmicpc.net/problem/2252
N , M = map(int, input().split())
table = [[0, i+1] for i in range(N)]
for _ in range(M):
    A , B = map(int, input().split())
    table[B-1][0] = table[A-1][0] + 1
    
table.sort()


for cost, num in table:
    print(num, end=' ')