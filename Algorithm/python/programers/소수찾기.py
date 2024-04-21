from itertools import permutations

def is_prime(number):
    if 1 >= number:
        return False

    for i in range(2, int(number**(1/2)) + 1):
        if number % i == 0:
            return False

    return True

def solution(numbers):
    return len(list(filter(is_prime, set(int(''.join(p)) for n in range(1, len(numbers)+1) for p in permutations(numbers, n)))))

