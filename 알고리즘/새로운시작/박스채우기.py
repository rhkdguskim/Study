# https://www.acmicpc.net/problem/1493
import sys
input = sys.stdin.readline

l, w, h = map(int, input().split()) # 가로, 세로, 높이
N = int(input()) # 큐브의 종류
cube = [0 for _ in range(N)]

for _ in range(N):
    a , b = map(int, input().split())
    cube[a] = b


def fillbox(l, w , h):
    if w == 0 and h == 0: # 모두 채웠을떄
        return
    
    if w == 0: # 가로를 모두 채웠다면 더이상 채울 필요가 없다.
        return 0
    
    # 가로, 세로, 높이에 넣을 수 있는 가장 큰 큐브를 찾는다.
    length = l
    width = w
    for i in range(len(cube), -1, -1):
        while cube[i]:
            if i <= l and i <= w and i <= h: # 큐브를 넣을 수 있다면 최대한 많이 넣는다.
                cube[i] -= 1
                w -= i
            else:
                break
    fillbox()
            
    
