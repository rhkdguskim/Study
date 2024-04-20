survey = ["AN", "CF", "MJ", "RT", "NA"] # 첫번째 비동의, 2번째 동의
choices = [5, 3, 2, 7, 5]


def solution(survey, choices):
    survayResult = dict()
    character = ['R','T','C','F','J','M','A','N']
    
    for data in character: # 성격유형 딕서너리 가중치 초기화
        survayResult[data] = 0
    
    length = len(survey)
    for i in range(length):
        if(1 <= choices[i] <= 3) : # 비동의 파트
            if(choices[i] == 1) :
                survayResult[survey[i][0]] += 3
            elif(choices[i] == 2):
                survayResult[survey[i][0]] += 2
            elif(choices[i] == 3):
                survayResult[survey[i][0]] += 1
        elif ( 5 <= choices[i] <= 7): # 동의 파트
            if(choices[i] == 5) :
                survayResult[survey[i][1]] += 1
            elif(choices[i] == 6):
                survayResult[survey[i][1]] += 2
            elif(choices[i] == 7):
                survayResult[survey[i][1]] += 3
                

    answer = ""
    # 유형 결과로 유형 판독하기
    if(survayResult['R'] >= survayResult['T']): # 1번 지표
        answer += 'R'
    else:
        answer += 'T'
    
    if(survayResult['C'] >= survayResult['F']): # 2번 지표
        answer += 'C'
    else:
        answer += 'F'
    
    if(survayResult['J'] >= survayResult['M']): # 3번 지표
        answer += 'J'
    else:
        answer += 'M'
    
    if(survayResult['A'] >= survayResult['N']): # 4번 지표
        answer += 'A'
    else:
        answer += 'N'
        
    return answer
    
solution(survey, choices)