# 1부터 6까지 적힌 주사위 네 개 있습니다. 네 주사위를 굴렸을때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.
# 네 주사위에서 나온 숫자가 모두 P로 같다면 1111 x p점을 얻습니다.
# 세주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나혼숫자가 q라면 (10 x p + q)^2 점을 얻습니다.
# 주사위가 두개 씩 같은 값이 나오면 p, q라고 하면 (p+q) x |p+q|점을 얻는다.
# 두주사위가 같고 나머지가 다르면 (q x r)
# 주사위가 모두 다르다면 가장 작은 숫자 값을 얻는다

def solution(a, b, c, d):
    nums = [a, b, c, d]
    counts = [nums.count(i) for i in nums]
    if max(counts) == 4: # 주사위가 모두 같은경우
        return a * 1111
    elif max(counts) == 3: # 주사위가 3개가 같은경우
        p = nums[counts.index(3)]
        q = nums[counts.index(1)]
        return (10 * p + q) ** 2
    elif max(counts) == 2:
        if min(counts) == 2: # 2개와 2개가 서로 같음
            return (a + c) * abs(a - c) if a == b else (a + b) * abs(a - b)
        else: # 2개와 서로다른 두 주사위
            p = nums[counts.index(2)]
            return (a * b * c * d) / p**2
    else: # 주사위가 모두 다름
        return min(nums)

print(solution(3,4,5,5))