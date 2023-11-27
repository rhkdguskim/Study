# https://www.acmicpc.net/problem/1744
import sys
def input():
    return sys.stdin.readline()

N = int(input())

plus = []
minus = []
zero = []

for _ in range(N):
    temp = int(input())
    if temp > 0:
        plus.append(temp)
    elif temp < 0 :
        minus.append(temp)
    else:
        zero.append(temp)

# 양수는 오름차순 정렬
plus.sort()

# 음수는 내림차순 정렬 (가장 작은 값이 맨뒤에 있다.)
minus.sort(reverse=True)

ans = 0
while len(plus) >= 2:
    num1 = plus.pop()
    num2 = plus.pop()
    if num1 == 1 or num2 == 1:
        ans += num1 + num2
    else:
        ans += num1 * num2

while len(minus) >= 2:
    num1 = minus.pop()
    num2 = minus.pop()
    ans += num1 * num2
    
if len(minus) > 0:
    if len(zero) > 0:
        ans += sum(plus)
    else:
        ans += sum(plus) + sum(minus)
else:
    ans += sum(plus)

print(ans)