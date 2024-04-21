# https://school.programmers.co.kr/learn/courses/30/lessons/42840
# 1번 수포자는 5개씩 돌아간다
# 2번 수포자는 8개씩 돌아간다
# 3번 수포자는 10개씩 돌아간다.
def solution(answers):
    person = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    solve = [0, 0, 0]
    for i, answer in enumerate(answers):
        for p in range(3):
            idx = i % len(person[p])
            if person[p][idx] == answer:
                solve[p] += 1

    return list(map(lambda x:x[1], filter(lambda x:x[0] == max(solve), [(solve[i], i+1) for i in range(3)])))
