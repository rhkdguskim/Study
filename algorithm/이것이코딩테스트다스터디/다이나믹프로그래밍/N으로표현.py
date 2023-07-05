import heapq

def solution(N, number):
    queue = []
    result = -1
    numstr = ''
    for i in range(1, 10):
        numstr += str(N)
        heapq.heappush(queue, [i, int(numstr)])

    while queue:
        depth, now = heapq.heappop(queue)
        if number == now or depth == 9:
            if depth == 9:
                result = -1
            else :
                result = depth
            break
        heapq.heappush(queue, [depth+1, now+N])
        heapq.heappush(queue, [depth+1, now-N])
        heapq.heappush(queue, [depth+1, now*N])
        heapq.heappush(queue, [depth+1, now//N])
        
    return result
    
print(solution(5,200))