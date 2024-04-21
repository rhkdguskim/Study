from collections import defaultdict
import heapq

def solution(genres, plays):
    album = defaultdict(lambda:[0, []])
    for i, (g, p) in enumerate(zip(genres, plays)):
        album[g][0] += -p
        heapq.heappush(album[g][1], (-p, i))

    answer = []
    for _, p_q in sorted(album.values()):
        for _ in range(2):
            if p_q:
                _, idx = heapq.heappop(p_q)
                answer.append(idx)

    return answer