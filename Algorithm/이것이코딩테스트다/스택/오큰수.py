# https://www.acmicpc.net/problem/17298
# 1. 스택을 만든다.
# 2. 하나씩 꺼내가면서 새로운 큐에 넣는다. ( 작은순으로 넣어야함 )
# 3. 하나씩 넣을때 이분탐색으로 넣을 자리를 찾는다. 만약 index가 0이라면 -1을 출력한다.
from bisect import bisect_left
from collections import deque
N = int(input())

array = list(map(int, input().split()))
newarray = []
result = deque()
while array:
    a = array.pop()
    idx = bisect_left(newarray, a)
    if len(newarray) > idx >= 0:
        if len(newarray) == 0:
            result.appendleft(-1)
        else:
            result.appendleft(newarray[idx])
    else:
        result.appendleft(-1)
        
    newarray.insert(idx, a)
    
print(*result)


N = int(input())
array = list(map(int, input().split()))

stack = []
result = []

for num in reversed(array):
    # 현재 숫자가 스택의 최상단 요소보다 크거나 같은 동안 스택에서 요소를 제거
    while stack and stack[-1] <= num:
        stack.pop()

    # 스택이 비어 있으면 -1을 결과에 추가
    if not stack:
        result.append(-1)
    else:  # 그렇지 않으면 스택의 최상단 요소를 결과에 추가
        result.append(stack[-1])

    # 현재 숫자를 스택에 추가
    stack.append(num)

# 결과를 올바른 순서로 출력
print(*reversed(result))