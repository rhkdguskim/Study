import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())

tree = [0 for _ in range(4*N)]
arr = [0 for _ in range(N+1)]

for i in range(1, N+1):
    arr[i] = int(input())

def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end)
    return tree[node]

def quary(node, start, end, left, right):
    if start > right or end < left:
        return 0

    if left <= start and right >= end:
        return tree[node]

    mid = (start + end) // 2
    return quary(node*2, start, mid, left, right) + quary(node*2+1, mid+1, end, left, right)


def update(node, start, end, index, diff):
    if index < start or end < index:
        # index가 노드 범위 밖이면 탐색을 중단한다.
        return

    # 노드를 diff 만큼 증가시킨다.
    tree[node] += diff

    if start != end:
        # 리프 노드가 아닌 경우 자식 노드를 update해준다.
        mid = (start + end) // 2
        update(node * 2, start, mid, index, diff)
        update(node * 2 + 1, mid + 1, end, index, diff)
    return


init(1,1, N)
for _ in range(K+M):
    a, b, c = map(int, input().split())
    if a == 1: # b번째수를 c로 바꾼다.
        diff = c - arr[b]
        arr[b] = c
        update(1, 1, N, b, diff)
    # a가 1인경우 업데이트, a가 2인경우 구간합 찾기
    else:
        print(quary(1, 1, N, b, c))