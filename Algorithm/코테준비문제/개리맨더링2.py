# https://www.acmicpc.net/problem/17779
from pprint import pprint
import sys
input = sys.stdin.readline

N = int(input())
total = 0
table = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1):
    temp = list(map(int, input().split()))
    for j in range(1, N+1):
        table[i][j] = temp[j-1]
def solve(x, y, d1, d2):
    city = [[0 for _ in range(N+1)] for _ in range(N+1)]
    # 경계선을 만든다.
    # 1번 경계선
    people = [0 for _ in range(5)]
    for t in range(d1+1):
        city[x+t][y-t] = 5

    # 2번 경계선
    for t in range(d2+1):
        city[x+t][y+t] = 5

    # 3번 경계선
    for t in range(d2+1):
        city[x+d1+t][y-d1+t] = 5

    # 4번 경계선
    for t in range(d1+1):
        city[x+d2+t][y+d2-t] = 5

    # 1번 도시
    for i in range(1, x+d1+1):
        for j in range(1, y+1):
            if city[i][j] == 5:
                break
            city[i][j] = 1

    # 2번 도시
    for i in range(1, x+d2+1):
        for j in range(N, y, -1):
            if city[i][j] == 5:
                break
            city[i][j] = 2

    # 3번 도시
    for i in range(x+d1, N+1):
        for j in range(1, y-d1+d2):
            if city[i][j] == 5:
                break
            city[i][j] = 3

    # 4번 도시
    for i in range(x+d2+1, N+1):
        for j in range(N, y+d2-d1-1, -1):
            if city[i][j] == 5:
                break
            city[i][j] = 4

    for i in range(1, N+1):
        for j in range(1, N+1):
            if city[i][j] == 0 or city[i][j] == 5:
                people[4] += table[i][j]
            elif city[i][j] == 1:
                people[0] += table[i][j]
            elif city[i][j] == 2:
                people[1] += table[i][j]
            elif city[i][j] == 3:
                people[2] += table[i][j]
            elif city[i][j] == 4:
                people[3] += table[i][j]

    result = abs(max(people) - min(people))
    return result



ans = 100 * 21 * 21
for x in range(1, N+1):
    for y in range(1, N+1):
        for d1 in range(1, N+1):
            for d2 in range(1, N+1):
                if N >= x + d1 + d2 and y-d1 >= 1 and N >= y+d2:
                    ans = min(solve(x ,y, d1, d2), ans)

print(ans)

