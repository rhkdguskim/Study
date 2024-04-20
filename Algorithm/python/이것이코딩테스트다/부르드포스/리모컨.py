# https://www.acmicpc.net/problem/1107
N = int(input()) # 목표숫자
M = int(input()) # 고장난 숫자 개수
brokennumber = []
if M > 0:
    brokennumber = list(map(int, input().split())) # 고장난 숫자 리스트

def calPushNumber(curnumber, goalnumber):
    if curnumber == 100:
        return 0
    
    if curnumber == goalnumber:
        return len(curnumber)
    else:
        return min(abs(100-goalnumber), len(curnumber) + abs(curnumber-goalnumber)) # 숫자의 길이 + 리모콘 -,+로 이동가능한 카운트
    
    
def makeAvailableNumber(targetNumber):
    strTargetNumber = str(targetNumber)
    num_of_digit = len(strTargetNumber)
    char = ''
    if brokennumber:
        for i in range(num_of_digit):
            minvalue = int(10e9)
            newchar = ''
            for k in range(0, 10):
                if k not in brokennumber: # 누를 수 있는 버튼중 가장 가까운 수를 선택한다.
                    #print(int(char + str(k)), int(strTargetNumber[0:i+1]))
                    cost = abs(int(char + str(k)) - int(strTargetNumber[0:i+1]))
                    if minvalue > cost:
                        minvalue = cost
                        newchar = str(k)
            #print(newchar)                
            char += newchar
            
        return char
    else:
        return strTargetNumber
            
if N == 100:
    print(0)
elif len(brokennumber) == 10:
    print(abs(100-N))
else:
    print(min(abs(100-N), len(str(N)) + abs(N-int(makeAvailableNumber(N))))) # 직접다 눌렀을때와 최적화된 넘버에서 직접눌렀을때 비교