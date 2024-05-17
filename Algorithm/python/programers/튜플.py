# https://school.programmers.co.kr/learn/courses/30/lessons/64065
# 입력을 list로 변환합니다.
# 리스트의 길이가 작은 기준으로 정렬합니다.
def solution(s :str):
    temp = s.lstrip('{').rstrip('}').split("},{")
    
    for i in range(len(temp)):
        temp[i] = list(map(int, temp[i].split(',')))
        
    temp.sort(key=len)
    answer = []
    
    for t in temp:
        for k in t:
            if k not in answer:
                answer.append(k)
    
    return answer