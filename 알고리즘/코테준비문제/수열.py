# 메모리 복잡도를 최적화 해야한다.

initNum = str(input())
left = int(input())
right = int(input())
N = int(input())

def makeArr(char, depth):
    if depth == N:
        if char == "1":
            return "132"
        elif char == "2":
            return "211"
        else:
            return "232"
        
    newchar = ""
    if char == "1":
        newchar = "132"
    elif char == "2":
        newchar = "211"
    else:
        newchar = "232"
    
    return makeArr(newchar[0], depth+1)+makeArr(newchar[1], depth+1)+makeArr(newchar[2], depth+1)

result = makeArr(initNum, 1)
if N > 0:
    print(result[left:right+1].count("1"), result[left:right+1].count("2"), result[left:right+1].count("3"))
else:
    print(initNum)