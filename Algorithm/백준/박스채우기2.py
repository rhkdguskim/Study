# https://www.acmicpc.net/problem/1493
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

l, w, h = map(int, input().split()) # 가로, 세로, 높이
N = int(input()) # 큐브의 종류
cube = []

for _ in range(N):
    a , b = map(int, input().split())
    cube.append([a, b])
    
cube.sort(reverse=True)

ans = 0
flag = False
def dfs(length, width, height):
    global ans, flag
    if length == 0 or width == 0 or height == 0: # 더이상 큐브를 넣을 수 없는 빈 박스이다.
        return
    
    flag = False
    size = 0
    for i in range(len(cube)):
        size = 2 ** cube[i][0]
        if cube[i][1] and length >= size and width >= size and height >= size: # 큐브의 개수가 존재하고 크기에 들어갈 수 있는 크기라면
            cube[i][1] -= 1
            flag = True
            ans += 1
            break
    
    # 넣을 수 있는 경우가 나온다면
    if flag:
        dfs(length, width, height-size) #위에 4x4x4
        dfs(size, width-size, size) #가로 4x0x0 = 0
        dfs(length-size, width, size) # 세로 0x4x4 = 0
        # 넣은 큐브의 사이즈를 제외한 박스를 분할정복탐색한다.
    else:
        return
    
dfs(l, w, h)
if flag:
    print(ans)
else:
    print(-1)
    