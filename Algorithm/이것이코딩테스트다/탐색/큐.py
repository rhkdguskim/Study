from collections import deque

queue = deque()
queue.append([1,1])
x, y= queue.popleft()

print(x, y)