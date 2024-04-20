mo = {'A','E','I','O','U'}

word = input()

def dfs(mocnt, jacnt, lcnt, depth):
    if mocnt >= 3 or jacnt >= 3:
        return 0
    
    if depth == len(word):
        if lcnt:
            return 1
        else:
            return 0
    
    result = 0
    if word[depth] == '_':
        # 모음일때
        result += dfs(mocnt+1,0,lcnt, depth+1) * len(mo)
        # L을 제외한 자음일때
        result += dfs(0,jacnt+1,lcnt, depth+1) * (25 - len(mo))
        # L일때
        result += dfs(0,jacnt+1, lcnt+1, depth+1) * 1
    else:
        if word[depth] in mo:
            result += dfs(mocnt+1,0, lcnt, depth+1)
        else:
            if word[depth] == 'L':
                result += dfs(0, jacnt+1, lcnt+1, depth+1)
            else:
                result += dfs(0, jacnt+1, lcnt, depth+1)
        
    return result
            

print(dfs(0,0,0,0))
