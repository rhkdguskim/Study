#https://www.acmicpc.net/problem/12919
S = str(input())
T = str(input())

findFlag = False
def charReverse(char):
    newchar = ""
    
    length = len(char) // 2
    arr = list(char)
    for i in range(length):
        arr[i], arr[len(arr)-1 - i] = arr[len(arr)-1 - i], arr[i]
        
    for c in arr:
        newchar += c
        
    return newchar


def AandB(char):
    global findFlag
    if len(char) == len(T):
        if char == T:
            findFlag = True
        return
                
            
    newchar1 = char + "A"
    newchar2 = char + "B"
    
    AandB(newchar1)
    AandB(charReverse(newchar2))
            
AandB(S)            
            
if findFlag:
    print(1)
else:
    print(0)
    