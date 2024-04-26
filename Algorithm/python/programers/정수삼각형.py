# 왼쪽에서 내려오는경우 ( 왼쪽 )
# 위에서 내려오는경우 ( 오른쪽 )
def solution(triangle):

    for i in range(1, len(triangle)):
        length = len(triangle[i-1])
        for j in range(len(triangle[i])):
            # 왼쪽에서 온경우
            left_value = 0
            if 0 <= j-1 < length:
                left_value = triangle[i-1][j-1] + triangle[i][j]
            # 오른쪽에서 온경우
            right_value = 0
            if 0 <= j < length:
                right_value = triangle[i-1][j] + triangle[i][j]

            triangle[i][j] = max(left_value, right_value, triangle[i][j])

    return max(triangle[-1])
