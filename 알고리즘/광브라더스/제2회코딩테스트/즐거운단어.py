alpa = {'A','B','C','D','E','F',"G",'H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}
mo = {'A','E','I','O','U'}
za = alpa - mo

word = input()

answer = 0
def dfs(char, depth):
    global answer
    if len(char) >= 3: # n-1과 n-2 값이 모임인지 자음인지 확인한다 ( 단, word의 현재길이가 3보다 크거나 같아야한다.)
        if char[-1] in mo: # 모음이라면
            if char[-2] in mo and char[-3] in mo:
                return
        if char[-1] in za:
            if char[-2] in za and char[-3] in za:
                return
    
    if len(word) == len(char): # 같아진다면 L이 있는지 확인하고 종료한다.
        if 'L' in char:
            answer += 1
        return
    
    if word[depth] == '_':
        for c in alpa: # 알파벳을 다 더해본뒤 
            char.append(c)
            dfs(char, depth+1)
            char.pop()
    else:
        char.append(word[depth])
        dfs(char, depth + 1)
        char.pop()
    
dfs(list(),0)
print(answer)