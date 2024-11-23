import sys
input = sys.stdin.readline

# 소수 집합 캐싱
prime_cache = set()

def solution(n):
    def is_prime(num):
        # 이미 캐싱된 소수는 바로 반환
        if num in prime_cache:
            return True
        
        if num < 2:
            return False
        
        # 소수 판별
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        
        # 소수로 확인되면 캐싱
        prime_cache.add(num)
        return True

    cnt = 0
    for i in range(n + 1, 2 * n + 1):
        if is_prime(i):
            cnt += 1
    return cnt

# 입력 처리
while True:
    try:
        n = int(input().strip())
        if n == 0:
            break
        print(solution(n))
    except ValueError:
        # EOF나 잘못된 입력 처리
        break