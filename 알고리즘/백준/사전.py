# https://www.acmicpc.net/problem/1256
import sys
from itertools import permutations

a = 'aaaaa'
b = 'bbbbb'

input = sys.stdin.readline
N, M, K = map(int, input().split())

a = [0 for _ in range(N)]
z = [1 for _ in range(M)]
lst = a + z
new_lst = set(permutations(lst, N+M))
new_list2 = sorted(list(new_lst))

for idx, n in enumerate(new_list2):
    print(n, idx+1)
    
print(''.join(str(new_list2[K-1])))