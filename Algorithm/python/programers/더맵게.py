import heapq

def solution(scoville, K):
    heapq.heapify(scoville)

    cnt = 0
    while len(scoville) >= 2 and K > scoville[0]:
        v1 = heapq.heappop(scoville)
        v2 = heapq.heappop(scoville)
        heapq.heappush(scoville, v1+(v2 * 2))
        cnt += 1

    if K > scoville[0]:
        return -1
    return cnt