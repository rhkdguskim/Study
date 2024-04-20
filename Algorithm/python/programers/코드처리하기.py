
def solution(code):
    mode = 0
    n = len(code)
    ret = ''
    for i in range(n):
        if(mode == 0) :
            if(code[i] != '1') :
                if(i % 2 == 0) :
                    ret += code[i]
            else :
                mode = 1
        else :
            if(code[i] != '1') :
                if(i % 2 == 1) :
                    ret += code[i]
            else :
                mode = 0
    if(ret == '') :
        return "EMPTY"
    else:
        return ret
    
print(solution("abc1abc1abc"))