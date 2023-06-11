from collections import deque
R, C = map(int,input().split())
arr = []
for _ in range(R):
    arr.append(input())

def addQueue(i, j, chr, queue):
    if (R > i >= 0 and C > j >= 0):
        if not arr[i][j] in chr:
            queue.append((i,j, chr+arr[i][j]))
            return True
        else :
            return False
    return False
        
def bfs(i,j):
    queue = deque()
    queue.append((i,j, arr[i][j]))
    max_score = 0
    while queue:
        y, x, chr = queue.popleft()
        max_score = max(max_score, len(chr))
        addQueue(y+1, x, chr, queue)
        addQueue(y, x+1, chr, queue)
        addQueue(y-1, x, chr, queue)
        addQueue(y, x-1, chr, queue)

    return max_score


print(bfs(0,0))