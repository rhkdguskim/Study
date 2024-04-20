# 선분 3개가 평행하게 놓여있습니다.
# 세 선분의 시작과 끝 좌표가 있고 두개 이상의 선분이 겹치는 부분의 길이를 구하시오
lines = [[0, 1], [2, 5], [3, 9]]
#lines = [[-1, 1], [1, 3], [3, 9]]
#lines = [[0, 5], [3, 9], [1, 10]]
def solution(lines):
    newarr = []
    newarr2 = []
    for data in lines:
        newarr2.append(data[0])
        newarr2.append(data[1])
        
    for i in range(lines[0][0], lines[0][1] +1):        
        newarr.append(i)
        
    for i in range(lines[1][0], lines[1][1] +1):
        newarr.append(i)
    
    for i in range(lines[2][0], lines[2][1] +1):
        newarr.append(i)
    
    result = 0    
    # 시작점과 끝점이 겹치는 부분 찾기
    for i in range(min(newarr2), max(newarr2) + 1):
        if(newarr2.count(i) > 1) :
            result-=1
    
    # 겹치는 선분 찾기
    pagedarr = []
    for i in range(min(newarr), max(newarr)+1):
        if(newarr.count(i) > 1):
            pagedarr.append(i)
            
    return max(pagedarr) - min(pagedarr) + result

solution(lines)