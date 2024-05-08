# https://school.programmers.co.kr/learn/courses/30/lessons/70130
# 길이가 2이 상의 짝수
# 부분수열중에서 길이가 가장 긴 스타수열의 길이 return
# 3개중 가장 긴 스타수열을 찾는다.
# 배열 a[:], a[1:], a[:len(a)-1]
# [5, 2, 3, 3, 5, 3]
# [5, 2, 3, 3, 5] 를 예를 들어 보자
# [5, 2, 3, 3], [2, 3, 3, 5], [5, 3, 3, 5], [5, 2, 3, 5], [5, 2, 3, 5]

def solution(a):
    n = len(a)
    def is_star(start, end):
        pair = {}
        for i in range(start, end, 2):
            if a[i] == a[i+1]:
                return set()
            else:
                pair[i] = {a[i], a[i + 1]}

        temp = set(a[start:end+1])
        for key in pair.keys():
            temp &= pair[key]

        #print(temp)
        return temp

    dp = [[0] * n for _ in range(n)]
    for i in range(0, n-1):
        dp[i][i+1] = is_star(i, i + 1)

    for k in range(3, n):
        for i in range(n-k):
            temp = is_star(i + k - 1, i + k) & is_star(i, i + k - 2)
            if len(temp):
                dp[i][i+k] = temp
            else:
                dp[i][i+k] = dp[i][i+k-1]

    print(dp)
    answer = -1
    return answer

#solution([5,2,3,3,5,3])
solution([0,3,3,0,7,2,0,2,2,0])
#solution([0])