# 양의 정수 n이 매개변수로 주어집니다. 
# n x n 배열에 1부터 n^2 까지 정수를 인덱스[0][0]부터 시계방향 나선형으로 배치한 이차원 배열을 return하는 함수를 작성하라

# 첫번째 나선반복 ( 오 -> 아 -> 왼 -> 위 ) n x n 배열에서
# 오른쪽은 n
# 아래는 n-1 오른쪽 -1
# 왼쪽은 n-1 오른쪽 -1
# 위쪽은 n-2 오른쪽 -2

# 두번째 나선반복
# n-2 오른쪽은 나선반복1의 위쪽과 같다
# n-3 왼쪽은 오른쪽 -1
# n-3 아래는 오른쪽 -1
# n-4 위쪽은 오른쪽 -2

def solution(n) :
    arr = [[0]*n for _ in range(n)] # 배열을 해당 크기로 초기화 합니다.
    toggle = (0, -1)
    shift = True
    arrow = ['E','S','W','N']
    arrowptr=0
    x = -1
    y = 0
    counter = 1

    while n > 0:
        if shift :
            n -= toggle[0]
            shift = False
        else:
            n += toggle[1]
            shift = True
        
        for _ in range(n):
            if arrow[arrowptr] == 'E':
                x += 1
            elif arrow[arrowptr] == 'S':
                y += 1
            elif arrow[arrowptr] == 'W':
                x -= 1
            elif arrow[arrowptr] == 'N':
                y -= 1
            
            arr[y][x] = counter
            counter += 1
        
        arrowptr += 1
        if(arrowptr == 4):
            arrowptr = 0
    
    return arr
    
print(solution(4))
