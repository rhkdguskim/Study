from collections import deque

N, K = map(int, input().split())
graph = [-1 for _ in range(100001)]  # Using -1 to represent unvisited
queue = deque()

queue.append(N)
graph[N] = N  # The parent of the starting point is itself.

while queue:
    X = queue.popleft()

    if X == K:
        path = [K]
        while X != graph[X]:  # Reconstruct the path using parents.
            path.append(graph[X])
            X = graph[X]
        print(len(path) - 1)  # Number of moves
        print(*reversed(path))
        break

    for next_X in [X*2, X-1, X+1]:
        if 0 <= next_X <= 100000 and graph[next_X] == -1:
            graph[next_X] = X  # Set the parent of next_X to X.
            queue.append(next_X)