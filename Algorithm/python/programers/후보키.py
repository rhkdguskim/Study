from itertools import combinations

def solution(relation):
    rows = len(relation)
    cols = len(relation[0])
    
    all_combinations = []
    # 컬럼의 모든 조합을 만든다.
    for length in range(1, cols + 1):
        all_combinations.extend(combinations(range(cols), length))
    
    unique_sets = []
    for cols in all_combinations:
        # 조합으로 튜플을 만들어 유일성을 체크한다.
        temp_set = {tuple(relation[r][c] for c in cols) for r in range(rows)}
        if len(temp_set) == rows:
            unique_sets.append(cols)
    
    # 최소성 검사
    answer = set(unique_sets)
    for i in unique_sets:
        for j in unique_sets:
            if i != j and set(i).issubset(set(j)):
                answer.discard(j)
    
    return len(answer)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))