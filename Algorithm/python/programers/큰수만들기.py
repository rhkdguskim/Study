# number 맨 앞 원소부터 순회한다.
# 스택을 이용하여 문제를 해결한다.
# 현재 원소가 스택의 마지막 원소보다 클경우 스택의 마지막원소가 더 큰값이 나올때까지 pop한다 ( 이때 pop 할때 숫자가 제거된다 )
# 다 순회를 했는데도 k가 남아있다면 남은 만큼 pop 한다
# 그리고 나머지를 출력하면 끝
def solution(number, k):
    stack = []
    for i in range(len(number)):
        cur = int(number[i])
        while stack and k and cur > stack[-1]:
            stack.pop()
            k -= 1

        stack.append(int(number[i]))

    if k > 0:
        for _ in range(k):
            stack.pop()

    return ''.join(map(str, stack))