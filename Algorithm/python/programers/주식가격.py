def solution(prices):
    # 스택자료구조를 활용하여, 스택의 마지막원소가 자기자신보다 작을경우 해당 인덱스의 길이의 차이를 갱신하고 pop시킨다.
    answer = [0 for _ in range(len(prices))]
    stack = []
    for i, p in enumerate(prices):
        # 현재 마지막 스택에서 p보다 클경우 주식은 하락했으므로 갱신
        while stack and stack[-1][1] > p:
            prev = stack.pop()
            answer[prev[0]] = i - prev[0]

        stack.append((i, p))

    # 마지막까지 스택에 남아있다면 끝까지 주식이 떨어지지 않았다.
    while stack:
        prev = stack.pop()
        answer[prev[0]] = len(prices) - 1 - prev[0]

    return answer