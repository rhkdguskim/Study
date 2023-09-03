# https://www.acmicpc.net/problem/1062
from itertools import combinations

N, K = map(int, input().split())
words = set(('a','n','t','i','c'))
alpabat = set(('b','d','e','f','g','h','j','k','l','m','o','p','q','r','s','u','v','w','x','y','z'))

charlist = list()

for _ in range(N):
    char = set(input())
    if set(words).issubset(char):
        charlist.append(char)
    
maxcounter = 0
visited = dict()
if K-5 > 0:
    for alpa in combinations(alpabat, K-5):
        counter = 0
        for char in charlist:
            newlist = alpa + ('a','n','t','i','c')
            if set(char).issubset(set(newlist)):
                counter += 1
                
        maxcounter = max(maxcounter,counter)
    
print(maxcounter)