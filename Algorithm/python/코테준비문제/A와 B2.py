#https://www.acmicpc.net/problem/12919
# 거꾸로 문제를 해결해 나아가야하는게 문제의 포인트이다.

S = str(input())
T = str(input())

findFlag = False

def AandB(char):
    global findFlag
    if findFlag:
        return
    
    if len(S) >= len(char):
        if char == S:
            findFlag = True
        return
                
            
    newchar1 = char[:len(char)-1]
    newchar2 = char[1:][::-1]
    if char[-1] == 'A':
        AandB(newchar1)
    if char[0] == 'B':
        AandB(newchar2)
            
AandB(T)            
            
if findFlag:
    print(1)
else:
    print(0)
    