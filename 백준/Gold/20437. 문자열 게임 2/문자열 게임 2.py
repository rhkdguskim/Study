import sys
from collections import defaultdict

input = sys.stdin.readline

for _ in range(int(input())):
    w_d = defaultdict(list)
    word = input().strip()
    K = int(input())
    for i, w in enumerate(word):
        w_d[w].append(i)
    
    ans = []
    for key in w_d.keys():
        arr = w_d[key]
        if len(arr) >= K:
            for i in range(len(arr) - K+1):
                l = arr[i+K-1] - arr[i] + 1
                ans.append(l)
                
    l = len(ans)
    if l == 0:
        print(-1)
    elif l == 1:
        print(ans[0], ans[0])
    else:
        ans.sort()
        print(ans[0], ans[-1])