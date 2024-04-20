# https://www.acmicpc.net/problem/1062
# 1부터 27까지 a,z라고 본다.
import sys
from itertools import combinations
input = sys.stdin.readline

N, K = map(int, input().split())
words = [0 for _ in range(N)]
for i in range(N):
    temp = str(input().strip())
    for j in range(len(temp)):
        cost = ord(temp[j]) - ord('a') + 1
        if not (words[i] & (1 << cost)):
            words[i] |= (1 << cost)

alpa = [i for i in range(1, 27)]
ans = 0
if K > 4:
    for check in combinations(alpa, K):
        temp = 0
        cnt = 0
        for c in check:
            temp |= (1 << c)

        for word in words:
            if (temp & word) == word:
                cnt += 1

        if cnt > ans:
            ans = cnt
    print(ans)
else:
    print(0)