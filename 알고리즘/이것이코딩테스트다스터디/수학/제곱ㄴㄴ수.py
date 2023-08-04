# https://www.acmicpc.net/problem/1016
import math
min, max = map(int, input().split())
visited = [1] * (max - min + 1) # 최대 1,000,000

def isValied(number):
    tryn = math.sqrt(number)
    temp = 2
    for _ in range(tryn):
        pass

print(sum(visited))