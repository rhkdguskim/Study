import sys
input = sys.stdin.readline

N = int(input())

def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

prime_num = [2, 3, 5, 7]
for i in range(1, N):
    new = []
    for i in range(10):
        for p in prime_num:
            num = int('{:d}{:d}'.format(p, i))
            if is_prime(num):
                new.append(num)
    prime_num = new
    
for s in sorted(prime_num):
    print(s)
    
        