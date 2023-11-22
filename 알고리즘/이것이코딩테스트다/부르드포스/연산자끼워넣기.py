# https://www.acmicpc.net/problem/1065
N = int(input())

counter = 0
for i in range(1, N+1): # 1부터 N까지
    # 한자리 일때는 조건없이 카운트
    if 0 < i < 10:
        counter += 1
    # 두자리 일대도 조건없이 카운트
    if 10 <= i < 100:
        counter += 1
    # 세자리
    string = str(i)
    if 100 <= i < 1000:
        if (int(string[0]) - int(string[1])) == (int(string[1]) - int(string[2])):
            counter += 1
            
print(counter)
    