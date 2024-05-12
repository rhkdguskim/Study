# 비트가 0이 있는지 확인한다.

def solution(numbers):
    answer = []
    for n in numbers:
        i = 1
        
        # 0이 있는 구간을 찾는다.
        while i <= n:
            ret = i != (n & i)
            if ret:
                break
            
            i = i * 2
        
        # 0이 존재한다면 i가 1인 경우는 1을 더해야하고 1이 아닌경우에는 그전단계를 더해주면 된다.
        # 예를들어 0xb01 라면 0xb10이 나오므로 0xb01을 더해주면 0xb10이 나온다.
        # i가 1일때만 1을 더하는 로직을 예외처리해주면 된다.
        # 0이 존재하지 않는다면 왼쪽에 1만 추가해주면 된다.
        if i != 1:
            n += i//2
        else:
            n += i
        
        answer.append(n)
        
    return answer