# https://www.acmicpc.net/problem/9252

str1 = str(input())
str2 = str(input())
length1 = len(str1)
length2 = len(str2)
dp = [[0 for _ in range(length2+1)] for _ in range(length1+1)]

for i in range(1, length1+1):
    for j in range(1, length2+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

arr = ''
count = 1
maxdp = dp[length1][length2]
print(maxdp)
i = length1
j = length2
while i >= 0 and j >= 0:
    if dp[i-1][j] == dp[i][j]:
        i -= 1
    elif dp[i][j-1] == dp[i][j]:
        j -= 1
    else:
        arr += str1[i-1]
        j -= 1
        i -= 1

reversechar = ''
for i in range(len(arr)-1, -1, -1):
    reversechar += arr[i]
    
print(reversechar)