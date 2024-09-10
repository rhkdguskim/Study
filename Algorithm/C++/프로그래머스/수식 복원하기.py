# https://school.programmers.co.kr/learn/courses/30/lessons/340210?language=python3
# 각 수식마다 가능한 진법수를 계산합니다.
# 겹치는 진법수를 계산합니다.
# 이제 하나씩 계산해보면서 값이 일치하는지 확인합니다.

def solution(expressions):
    answer = []
    def has(expression : str):
        num, ex, num2, eq, num3 = expression.split(' ')
        return num3 == 'X'
    
    def not_has(expression : str):
        num, ex, num2, eq, num3 = expression.split(' ')
        return num3 != 'X'
    
    def getjinsu(expression : str):
        # 각 자리수에서 가장 큰값을 찾는다.
        num, ex, num2, _, num3 = expression.split(' ')
        if  num3 != 'X':
            max_v = max(int(num[-1]), int(num2[-1]), int(num3[-1]))
        else:
            max_v = max(int(num[-1]), int(num2[-1]))
                
        return [i for i in range(max_v+1, 10)]
    
    def jinsu_filter(expression : str, max_v):
        number = []
        num, ex, num2, _, num3 = expression.split(' ')
        # 이제 max_v 이후의 값에서 진수계산이 올바른것을 찾는다.
        for c in range(max_v+1, 10):
            temp = int(num, c)
            temp2 = int(num2, c)
            temp3 = int(num3, c)
            ret = False
            if ex == '+':
                ret = temp + temp2 == temp3
            else:
                ret = temp - temp2 == temp3
            
            if ret:
                number.append(c)
        
        return number
        
        
    result = list(filter(has, expressions))
    check = list(filter(not_has, expressions))
    
    print(check)
    for c in check:
        print(getjinsu(c))
    
    
    return answer

solution(["1 + 1 = 2", "1 + 3 = 4", "1 + 5 = X", "1 + 2 = X"])