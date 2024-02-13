# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각중에서 3이 하나라도 포함된
# 모든 경우의 수를 구하는 프로그램을 작성하시오.

N = int(input())
hour = 0
min = 0
sec = 0
counter = 0
while( N+1 > hour):
    
    # 1초를 증가시킨다.
    sec += 1
    
    if(sec == 60): # 60초 카운트시 분 증가
        sec = 0
        min += 1
    
    if (min == 60): # 60분 카운트시 시 증가
        min = 0
        hour += 1
    
    if("3" in str(sec) + str(min) + str(hour)):
        counter += 1
        
    print(str(hour) + str(min) + str(sec))
        
print(counter)