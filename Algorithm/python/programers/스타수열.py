# https://school.programmers.co.kr/learn/courses/30/lessons/70130
# 길이가 2이 상의 짝수
# 부분수열중에서 길이가 가장 긴 스타수열의 길이 return
# 3개중 가장 긴 스타수열을 찾는다.
# 배열 a[:], a[1:], a[:len(a)-1]
# [5, 2, 3, 3, 5, 3]
# [5, 2, 3, 3, 5] 를 예를 들어 보자
# [5, 2, 3, 3], [2, 3, 3, 5], [5, 3, 3, 5], [5, 2, 3, 5], [5, 2, 3, 5]
# 특정 구간을 담는 교집합 원소
# 특정 구간의 스타수열의 최대 길이
from collections import defaultdict
def solution(a):
    n = len(a)
    a = [a[0]] + a + [a[-1]]
    chk = [-1] * (n+2)
    cnt = defaultdict(int)
    answer = 0
    for i in range(1, n+1):
        if a[i-1] != a[i] and chk[i-1] != a[i]:
            chk[i-1] = a[i]
            cnt[a[i]] += 1
        elif a[i+1] != a[i] and chk[i+1] != a[i]:
            chk[i+1] = a[i]
            cnt[a[i]] += 1

        answer = max(answer, cnt[a[i]]*2)

    return answer