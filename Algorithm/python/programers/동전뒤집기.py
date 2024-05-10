# https://school.programmers.co.kr/learn/courses/30/lessons/131703
import sys

def solution(beginning, target):
    rows = len(beginning)
    columns = len(beginning[0])
    flipped = [[1 - beginning[i][j] for j in range(columns)] for i in range(rows)]
    answer = sys.maxsize

    def check(source, target):
        cnt = 0
        for i in range(columns):
            if source[0][i] != target[0][i]:
                cnt += 1
                for j in range(1, rows):
                    if source[j][i] == target[j][i]:
                        return False, 0
            else:
                for j in range(1, rows):
                    if source[j][i] != target[j][i]:
                        return False, 0
        return True, cnt

    for i in range(2 ** rows):
        source = []
        cnt = 0
        binary = bin(i)[2:].zfill(rows)  # 비트 길이를 rows만큼 패딩
        for k in range(rows):
            if binary[k] == '1':
                source.append(flipped[k])
                cnt += 1
            else:
                source.append(beginning[k])

        valid, col_flips = check(source, target)
        if valid:
            answer = min(answer, col_flips + cnt)

    return answer if answer != sys.maxsize else -1