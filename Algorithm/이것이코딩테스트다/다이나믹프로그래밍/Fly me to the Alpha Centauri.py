# https://www.acmicpc.net/problem/1011
T = int(input())

def distance(cost):
    count = 0  # 이동 횟수
    move = 1  # count별 빈도수
    move_plus = 0  # 이동한 거리의 합
    while move_plus < cost :
        count += 1
        move_plus += move  # count 수에 해당하는 move를 더함
        if count % 2 == 0 :  # count가 2의 배수일 때, 
            move += 1  
    
    return count
    
    

for _ in range(T):
    x, y = map(int, input().split())
    print(distance(y-x))