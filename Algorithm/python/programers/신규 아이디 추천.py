# https://school.programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id : str):
    new_id = list(new_id)
    n = len(new_id)
    # 대응되는 대문자를 소문자로 치환한다.
    for i in range(n):
        if new_id[i].isalpha():
            new_id[i] = new_id[i].lower()
    
    answer = ''
    # 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표를 제외한 모든 문자를 제거
    for i in range(n):
        # 마침표에서 2번 이상 연속된 부분을 하나의 마침표로 치환한다.
        if answer and answer[-1] == '.' and new_id[i] == '.':
            continue
        
        if new_id[i].isalpha() or new_id[i].isnumeric() or new_id[i] == '-' or new_id[i] == '_' or new_id[i] == '.':
            answer += new_id[i]
        
    
    # 처음와 끝에 .이 존재하면 제거
    answer = answer.lstrip('.')
    answer = answer.rstrip('.')
    
    if len(answer) == 0:
        answer += 'a'
    
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:14]
    
    while 2 >= len(answer):
        answer += answer[-1]
    
    return answer