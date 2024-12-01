import sys

input = sys.stdin.readline

N, r, c = map(int, input().split())
        
# r은 x축, c는 y축
def dfs(r, c, n):
    if n == 0:
        return 0
    
    c1 = pow(2, n-1)
    c2 = pow(2, n)
    offset = c1 * c1
    # 1사분면
    if 0 <= r < c1 and 0 <= c < c1:
        offset *= 0
    # 2사분면
    elif c1 <= r < c2 and 0 <= c < c1:
        offset *= 1
    # 3사분면
    elif 0 <= r < c1 and c1 <= c < c2:
        offset *= 2
    # 4사분면
    else:
        offset *= 3
    return dfs(r % c1, c % c1, n-1) + offset

print(dfs(c, r, N))