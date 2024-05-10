# https://school.programmers.co.kr/learn/courses/30/lessons/12983
#

def solution(strs, t):
    dp = {}
    n = len(t)
    for s in strs:
        dp[s] = 1

    while t not in dp:
        new_dp = {}
        for key in dp.keys():
            for s in strs:
                new_key = key + s
                new_length = len(new_key)
                cost = dp[key] + 1
                if n >= new_length and t[:new_length] == new_key:
                    if new_key not in new_dp:
                        new_dp[new_key] = cost
                    else:
                        if new_dp[new_key] > cost:
                            new_dp[new_key] = cost

        if len(new_dp) == 0:
            return -1

        dp = new_dp

    return dp[t]