# https://www.acmicpc.net/problem/1316
N = int(input())
result = N
for _ in range(N):
    char = str(input())
    chardic = dict()
    prev = ''
    for i in range(len(char)):
        if prev != char[i]: # 이전 단어가 바뀌었을때만 떨어진 문자를 체크한다.
            if char[i] in chardic:
                result -= 1
                break
            else:
                chardic[char[i]] = True
            
        prev = char[i]
        
print(result)