# 점 네 개의 좌표를 담은 이차원 배열 dots가 다음과 같이 매개변수로 주어집니다.
# 주어진 네 개의 점을 두 개씩 이었을때, 두 직선이 평행이 되는 경우가 있으면 1을 없으면 0을 return 하는 solution 함수를 완성해보세요

dots = [[1, 4], [9, 2], [3, 8], [11, 6]]
def solution(dots):
    if(dots[0] != dots[3] and dots[1] != dots[2]):
        if(dots[1][0] - dots[0][0] != 0 and dots[3][0] - dots[2][0]) :
            기울기 = (dots[1][1] - dots[0][1])/(dots[1][0] - dots[0][0])
            기울기2 = (dots[3][1] - dots[2][1])/(dots[3][0] - dots[2][0])
        
            if(기울기 == 기울기2):
                return 1
            else :
                return 0
        else :
            return 0
    else :
        return 0

solution(dots)




