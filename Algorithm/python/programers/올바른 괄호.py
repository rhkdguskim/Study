# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    # 스택에 값이 있고 ')'를 만다면 마지막 스택이 '('인경우가 올바른 경우이다. 만약 ')'를 만난다면 올바르지 않는 괄호이다.
    stack = []
    for c in s:
        if c == ')':
            if not stack:
                return False
            elif stack[-1] == ')':
                return False
            else:
                stack.pop()
        else:
            stack.append(c)
            
    return len(stack) == 0