rank = [3, 7, 2, 5, 4, 6, 1]
attendance = [False, True, True, True, True, False, False]

def solution(rank, attendance):
    students = dict()
    n = len(rank)
    for i in range(n): # student의 딕셔너리 만들기
        students[rank[i]] = attendance[i]
    
    applyed = []
    for student in range(1, len(students)+1) : # 3명의 학생을 선발합니다.
        if(students[student]): # 선발 가능한 학생만 선발합니다.
            applyed.append(student)
        
        if(len(applyed) == 3): # 3명을 선발하면 선발을 중지한다.
            break
        
    applyed = sorted(applyed)
    print(applyed)
    answer = 10000 * rank.index(applyed[0])+ 100 * rank.index(applyed[1]) + rank.index(applyed[2])
    print(answer)
    
    
    return answer

solution(rank,attendance)