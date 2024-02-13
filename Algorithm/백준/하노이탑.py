# https://www.acmicpc.net/problem/1914
import sys
input = sys.stdin.readline

N = int(input())

ans = []
def hanoi(n, start, end, through):
    if n == 1:
        print(start, end)
        ans.append((start, end))
        return
        
    hanoi(n-1, start, through, end)
    print(start, end)
    ans.append((start, end))
    hanoi(n-1, through, end, start)
    



print(pow(2,N) - 1) # 하노이 경우의 수는 2^n-1

if N <= 20:
    hanoi(N, 1, 3, 2)