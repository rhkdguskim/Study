# https://www.acmicpc.net/problem/2141
import sys
input = sys.stdin.readline

N = int(input())

village = []
all_people = 0
for _ in range(N):
    x, people = map(int, input().split())
    village.append((x, people))
    all_people += people

village.sort(key=lambda x:x[0])

acc_people = 0
for i in range(N):
    acc_people += village[i][1]
    if acc_people >= all_people / 2:
        print(village[i][0])
        break