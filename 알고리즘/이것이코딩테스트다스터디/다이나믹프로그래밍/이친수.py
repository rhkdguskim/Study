# https://www.acmicpc.net/problem/2193
N = int(input())

zero = [0 for _ in range(N)]
one = [0 for _ in range(N)]

if N == 1 or N == 2:
    print(1)
else:
    zero[2] = 1
    one[2] = 1
    for i in range(3, N):
        zero[i] = zero[i-1] + one[i-1]
        one[i] = zero[i-1]
        
    print(zero[N-1]+one[N-1])