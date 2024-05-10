# 첫번째 스티커를 땐 경우
# 첫번째 스티커를 때지 않은경우 중 최대값
def solution(sticker):
    n = len(sticker)
    if n == 1:
        return sticker[-1]

    first_dp = [0] * n
    last_dp = [0] * n

    first_dp[0] = sticker[0]
    # 1번스티커을 붙힌경우 2번스티커를 붙힌경우중 최대값
    first_dp[1] = max(sticker[0], sticker[1])
    # 2번 스티커를 붙힌게 최대값이다 ( 1번 스티커를 붙히지 않는경우라고 가정하기때문 )
    last_dp[1] = sticker[1]
    for i in range(2, n):
        if i == n - 1:
            last_dp[i] = last_dp[i-2] + sticker[i]
            first_dp[i] = first_dp[i-1]
        else:
            first_dp[i] = max(first_dp[i - 2] + sticker[i], first_dp[i - 1])
            last_dp[i] = max(last_dp[i-2] + sticker[i], last_dp[i-1])

    return max(last_dp[-1], first_dp[-1])