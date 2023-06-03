# 개인 정보 n개가 있습니다. 각 약관마다 개인정보 보관 유효기간이 정해져있습니다.
# 모든 달은 28일까지있고 개인정보를 파기해라
# privacies에서 파기해야할 정보를 구하여라

today = "2022.05.19" # 오늘날짜
terms = ["A 6", "B 12", "C 3"] # 약관종류 + 유효기간(달)
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"] # 개인정보

def solution(today, terms, privacies):
    totalday = 0
    year, month, day = today.split(".") # 오늘 날짜 파싱
    totalday = (int(year)*12*28) + (int(month)*28) + int(day) # day단위로 계산계산하여 바꾼다
    newterms = dict()
    for data in terms:
        data = data.split()
        newterms[data[0]] = totalday - int(data[1])*28
    answer = []
    idx = 1
    for data in privacies:
        data = data.split()
        year, month, day = data[0].split(".") # 오늘 날짜 파싱
        data[0] = (int(year)*12*28) + (int(month)*28) + int(day) # day단위로 계산계산하여 바꾼다
        if(newterms[data[1]] >= data[0]):
            answer.append(idx)
        idx += 1
            
    return answer
    
solution(today, terms, privacies)