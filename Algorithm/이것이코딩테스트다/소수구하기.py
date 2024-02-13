#https://www.acmicpc.net/problem/1929
M, N = map(int, input().split())

table = [False] * 1000001 # 소수가 아닌수
table[1] = True # 1은 소수가 아니다.
def isPrime(number):
    n = int(number ** 0.5)
    for i in range(2, n+1): # 제곱수까지 나누어 본다.
        if number % i == 0: # 제곱수까지 나누었을때 나누어 떨어지면 약수가 아니다.
            return False
        
    return True # 나누어 떨어졌으면 약수이다.

primelist = [] # 소수를 담는 리스트
for num in range(M, N+1):
    if isPrime(num) and not table[num]:
        primelist.append(num)
        for i in range(num * 2 , N+1, num):
            table[i] = True

for number in primelist:
    print(number)
    
