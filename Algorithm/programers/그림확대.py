# 직사각형 형태의 그림 파일이 있고, 이 그림파일은 1x1 크기의 정사각형 크기의 픽셀로 이루어져 있다.
# 문자열 picture 정수과 k매개 변수로 주어질때 그림 파일을 세로 x가로 k배 늘린 그림 파일을 나타내도록 하는 문자열 배열을 return 하는 함수를 만들어주세요
picture = [".xx...xx.", "x..x.x..x", "x...x...x", ".x.....x.", "..x...x..", "...x.x...", "....x...."]
k = 2
def solution(picture, k):
    answer = []
    
    for data in picture:
        newchar = ""
        for char in data:
            newchar += char * k
        
        for _ in range(k):
            answer.append(newchar)
    
    return answer

solution(picture, k)

