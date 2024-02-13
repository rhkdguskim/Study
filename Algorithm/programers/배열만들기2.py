# 정수 l과 r이 주어졌을때, l이상 r이하의 정수중에서 숫자 '0' 과 '5'로만 
# 이루어진 모든 정수를 오름차순으로 지정한 배열을 return 하는 soulution 함수를 완성하세요.

def solution(l, r):
    answer = []
    for number in range(l, r+1):
        if (number % 5 == 0 or number % 5 == 5):
            if not (notcontainnumber(number)) :
                answer.append(number)
            
    if len(answer) == 0 :
        return [-1]
    else :
        return answer

def notcontainnumber(number) :
    for digit in str(number):
        if (digit != '0' and digit !='5'):
            return True
    
    return False

solution(5,555)