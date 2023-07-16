# https://www.acmicpc.net/problem/5582
str1 = input()
str2 = input()

length1 = len(str1)
length2 = len(str2)

dp = [[0 for _ in range(length2+1)] for _ in range (length1+1)]

maxvalue = 0
for i in range(1, length1+1):
    for j in range(1, length2+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
            maxvalue = max(maxvalue, dp[i][j])
            
print(maxvalue)