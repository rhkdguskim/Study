# https://www.acmicpc.net/problem/9251
# 두 문자열이 같은경우
# 두 문자열이 다른경우
import sys
input = sys.stdin.readline
#sys.setrecursionlimit(int(1e9))

# 탑다운방식
temp = str(input().strip()) # ACAYKP
temp2 = str(input().strip()) # CAPCAK

dp = [[0 for _ in range(len(temp2))] for _ in range(len(temp))]

# def lcs(depth, depth2):
#     if depth == len(temp) or depth2 == len(temp2): # 길이의 범위를 벗어난경우
#         return 0
    
#     if dp[depth][depth2] != -1:
#         return dp[depth][depth2]
    
#     if temp[depth] == temp2[depth2]:
#         dp[depth][depth2] = lcs(depth+1, depth2+1) + 1
#     else:
#         dp[depth][depth2] = max(lcs(depth+1, depth2), lcs(depth, depth2+1))
        
#     return dp[depth][depth2]  
    
# print(lcs(0, 0))

# 바톰업 방식
for i in range(len(temp)):
    for j in range(len(temp2)):
        if temp[i] == temp2[j]:
            if i-1 >= 0 and j-1 >= 0:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = 1
        else:
            if i-1 >= 0:
                dp[i][j] = max(dp[i-1][j], dp[i][j])
                
            if j-1 >= 0:
                dp[i][j] = max(dp[i][j-1], dp[i][j])
            
print(dp[len(temp)-1][len(temp2)-1])