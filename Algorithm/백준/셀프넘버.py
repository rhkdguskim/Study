# https://www.acmicpc.net/problem/4673
# 문제분석
# 1, 2, 4, 8, 16, 24, 30, 33, 39, 51 ... # 셀프넘버 1로부터 시작
# 3, 6, 12, 15, 21, ...

self_number = []
visited = [False for _ in range(10001)]

def dfs(n):
    
    if n > 10000:
        return
    
    visited[n] = True
    
    total = n
    temp = n
    while temp > 0:
        total += (temp % 10)
        temp //= 10
        
    dfs(total)
        
        

for i in range(1, 10001):
    if not visited[i]:
        self_number.append(i)
        dfs(i)
        
for num in self_number:
    print(num)