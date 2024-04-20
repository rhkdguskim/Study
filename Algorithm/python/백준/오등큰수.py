# https://www.acmicpc.net/problem/17299
# 오등큰수로 정렬을 한다. (오등큰수, 인덱스) ( 인덱스는 단하나만 갖는데, 가장 오른쪽에 있는 값으로 선정한다.)

# 카운트를 한다. ( 해쉬 맵 )
# [1, 1, 2, 3, 4, 2, 1]
# [3, 3, 2, 1, 1, 2, 3]
# [3, 3, 2, 1, 1, 2, -1]
# [3, 3, 2, 1, 1, 1, -1]

# 거꾸로 순회하면서, 더큰수가 있는지 확인한다.
# 스택의 마지막원소가 자기자신보다 큰지 확인한다. 크면 그값으로 초기화한다.
# 스택의 마지막원소가 자기자신보다 작으면 모든것을 pop 하고 자기자신을 push 하고 -1을 넣는다.

import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
counter = [0 for _ in range(1000001)]

for i in range(N):
    counter[data[i]] += 1

stack = []
result = []
for i in range(N-1, -1, -1):
    while stack and stack[-1][0] <= counter[data[i]]:
        stack.pop()
        
    if stack and stack[-1][0] > counter[data[i]]:
        result.append(stack[-1][1])
    else:
        result.append(-1)
        
    stack.append((counter[data[i]], data[i]))

print(' '.join(map(str, reversed(result))))


