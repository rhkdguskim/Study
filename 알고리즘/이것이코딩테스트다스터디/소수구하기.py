#https://www.acmicpc.net/problem/1929
M, N = map(int, input().split())

table = [True] * 10001 # 소수가 아닌수

def isPrime(number):
    n = int(number ** 0.5)
    n += 1
    for i in range(2, n): # 제곱수까지 나누어 본다.
        if number % i == 0:
            return False
        
    return True

for num in range(2, int(10000 ** 0.5) + 1):
    if isPrime(num):
        num2 = num * 2
        while num2 <=10000:
            table[num2] = True
    
