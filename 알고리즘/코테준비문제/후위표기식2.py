# https://www.acmicpc.net/problem/1935
N = int(input())
number = [0 for _ in range(N)]
expression = input()

stack = []

for i in range(N):
    number[i] = int(input())
    
print
for char in expression:
    if char.isalpha():
        stack.append(number[ord(char) - ord('A')])
    else:
        cost = 0
        num2, num1 = stack.pop(), stack.pop()
        if char == '*':
            cost = num1 * num2
        elif char == '/':
            cost = num1 / num2
        elif char == '+':
            cost = num1 + num2
        elif char == '-':
            cost = num1 - num2
        
        stack.append(cost)
        
print("{:.2f}".format(stack[0]))