from itertools import permutations, chain

def solution(s : list):
    answer = []
    for char in s:
        temp = ''
        cnt_1 = 0
        cnt_110 = 0
        for c in char:
            if c == '0':
                # 110
                if cnt_1 >= 2:
                   cnt_110 += 1
                   cnt_1 -= 2
                # 0, 10
                else:
                    temp += '1' * cnt_1 + c
                    cnt_1 = 0
            else:
                cnt_1 += 1
        
        answer.append(temp + '110' * cnt_110 + '1'*cnt_1)
        
    return answer