import sys
input = sys.stdin.readline

N, K = map(int, input().split())

cnt = 0
while bin(N)[2:].count('1') > K: 
    cnt += N&-N
    N += N&-N
    
print(cnt)