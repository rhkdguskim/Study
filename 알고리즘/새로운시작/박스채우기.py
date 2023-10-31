# https://www.acmicpc.net/problem/1493
import sys
input = sys.stdin.readline

l, w, h = map(int, input().split()) # 가로, 세로, 높이
N = int(input()) # 큐브의 종류
cube = []

for _ in range(N):
    a , b = map(int, input().split())
    cube.append((a, b))
    
cube.sort(reverse=True)


ans = 0
total_size = 0
for idx, cnt in cube:
    total_size *= 8 # 4x4 -> 2x2로 갈때 비교하기위해서는 8배 차이가나서 8을 곱해준다.
    size = 2 ** idx
    new_cnt = (l//size) * (w//size) * (h//size) - total_size # 6x5x5 박스에서 5x5x5의 크기를 구할수 있는 사이즈는 1개로 구할 수 있다.
    # 음수가 나올 경우를 생각해야하는데, 4x4x4에서 1개를 채웠다면 2x2x2에서는 더 많은 개수로 채울 수 있기때문에 음수가 나오지 않는다.
    fill = min(new_cnt, cnt) # 채울 수 있는 최소 개수를 구한다.
    
    ans += fill # 갯수를 채운다.
    total_size += fill # 박스에 채운다.
    
if l*w*h == total_size:
    print(ans)
else:
    print(-1)