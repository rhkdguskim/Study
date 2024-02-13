# https://www.acmicpc.net/problem/18310
import sys
input = sys.stdin.readline

N = int(input().strip())
home = list(map(int, input().split()))

home.sort()

print(home[(N-1)//2])