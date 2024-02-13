# https://www.acmicpc.net/problem/16638
N = int(input())
expression = str(input())

maxvalue = -int(1e10)
def calExpression(current,depth):
    global maxvalue
    if depth == N:
        maxvalue = max(maxvalue, eval(current))
        return
    
    
    newcal1 = current + expression[depth] + expression[depth + 1] # 괄호연산 추가되지않은식
    newcal2 = current[:len(current)-1] + '('+ current[-1] + expression[depth] + expression[depth + 1] + ')' # 괄호연산을 추가 한 식
    newdepth = depth + 2
    if expression[depth] == '*': # 곱하기인 경우에는 그냥 붙힌다 괄호의 우선순위가 상관 없기 때문이다.
        calExpression(newcal1, newdepth)
    else:
        if current[-1] == ')': # 괄호가 이미 추가되어있다면 괄호연산을 하지 않는 값을 추가해야한다.
            calExpression(newcal1, newdepth) # 연산자와 숫자를 더한다.
        else:    
            calExpression(newcal1, depth + 2) # 괄호를 계산한것
            calExpression(newcal2, depth + 2) # 괄호를 계산하지 않을것
      
calExpression(expression[0], 1)      
print(maxvalue)