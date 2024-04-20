# https://www.acmicpc.net/problem/1038
# N번째 감소하는 수를 출력
N = int(input())

dp = [[] for _ in range(10)]
for i in range(10):
    dp[i].append(i)

result = [0,1,2,3,4,5,6,7,8,9]
for i in range(1, 10): # 자리수 반복 ( 두번째 자리수 부터 시작)
    temp_list = [[] for _ in range(10)]
    for j in range(1, 10):
        for k in range(j):
            for num in dp[k]:
                temp_list[j].append(int(str(j) + str(num)))
                result.append(int(str(j) + str(num)))
    
    dp = temp_list

if len(result) > N:
    print(result[N])
else:
    print(-1)
        