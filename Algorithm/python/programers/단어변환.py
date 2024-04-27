# https://school.programmers.co.kr/learn/courses/30/lessons/43163
# words 끼리의 가중치를 계산하여 만약 같은 단어가 1개이라면 다음단어로 이동 할 수 있다.
# 딕셔너리에 움직인 가중치를 두어서 이미 방문한 단어는 재방문 하지 않도록 한다.
from collections import deque, defaultdict

def solution(begin, target, words):
    edge = defaultdict(list)
    visited = defaultdict(int)
    words.append(begin)

    for w1 in words:
        visited[w1] = 10000
        for w2 in words:
            if w1 != w2 and check_word(w1, w2):
                edge[w1].append(w2)


    queue = deque()

    queue.append((begin, 0))
    visited[begin] = 0

    while queue:
        word, cost = queue.popleft()
        if word == target:
            return cost

        for next in edge[word]:
            if visited[next] > cost+1:
                visited[next] = cost+1
                queue.append((next, cost+1))

    return 0

def check_word(w1, w2):
    cnt = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            cnt += 1

    return cnt == 1