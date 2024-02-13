s = "aukks"
skip = "wbqd"
index = 5

def solution(s, skip, index):
    length = len(s)
    answer = ''
    for i in range(length):
        startchar = s[i]
        counter = index
        for i in range(1, index+1):
            if(chr(ord(startchar) + i) in skip) :
                counter += 1
        
        
        print(ord("z"))
        if('z' < chr(ord(startchar) + counter)) :
            print(ord(startchar) + counter - 26)
            answer += chr(ord(startchar) + counter - 26)
        else :
            answer += chr(ord(startchar) + counter)
    print(answer)
    return answer
    
solution(s,skip,index)