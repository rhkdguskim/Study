#https://www.acmicpc.net/problem/12919
from copy import deepcopy
S = str(input())
T = str(input())


findFlag = False
def AandB(char):
    global findFlag
    if len(char) == len(T):
        print(char, T)
        if char == T:
            findFlag = True
        return
            
    newchar1 = char + "A"
    newchar2 = char + "B"
    
    AandB(newchar1)
    AandB(newchar2)
            
AandB(S)            
            
if findFlag:
    print(1)
else:
    print(0)
    