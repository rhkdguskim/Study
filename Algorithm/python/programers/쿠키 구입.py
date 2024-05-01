# https://school.programmers.co.kr/learn/courses/30/lessons/49995

# 쿠키의 길이가 2000이니, N^2으로 문제 접근하자.
# 반으로 쪼갠뒤 투포인터를 이용하여 sum 값을 확인해 나아가 본다.
def solution(cookie):
    if len(cookie) == 1:
        return 0

    answer = 0
    for i in range(1, len(cookie)):
        l_p = 0
        r_p = len(cookie)
        l_sum = sum(cookie[l_p:i])
        r_sum = sum(cookie[i:r_p + 1])

        while r_p > l_p:
            if l_sum == r_sum:
                answer = max(answer,l_sum)
                break
            elif l_sum > r_sum:
                l_sum -= cookie[l_p]
                l_p += 1
            else:
                r_sum -= cookie[r_p-1]
                r_p -= 1

    return answer