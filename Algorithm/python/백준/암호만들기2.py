import sys
from itertools import combinations

input = sys.stdin.readline
mo_list = set(['a', 'e', 'i', 'o', 'u'])
L, C = map(int, input().split())
words = list(map(str, input().split()))
words.sort()

for w in combinations(words, L):
    mo_cnt = len(set(w) & mo_list)
    if mo_cnt >= 1 and len(w) - mo_cnt >= 2:
        print(''.join(w))