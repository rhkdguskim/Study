# https://www.acmicpc.net/problem/1958
import sys
input = sys.stdin.readline

temp1 = str(input().strip())
temp2 = str(input().strip())
temp3 = str(input().strip())

length = len(temp1)
length2 = len(temp2)
length3 = len(temp3)

dp = [[[-1 for _ in range(length3+1)] for _ in range(length2+1)] for _ in range(length+1)]

def lcs(char1, char2, char3):
    len1 = len(char1)
    len2 = len(char2)
    len3 = len(char3)
    
    if len1 == 0 or len2 == 0 or len3 == 0:
        return 0
    
    if dp[len1][len2][len3] != -1:
        return dp[len1][len2][len3]
    
    dp[len1][len2][len3] = 0
    
    if char1[-1] == char2[-1] and char1[-1] == char3[-1]:
        dp[len1][len2][len3] = lcs(char1[:len1-1], char2[:len2-1], char3[:len3-1]) + 1
    else:
        dp[len1][len2][len3] = max(lcs(char1[:len1-1], char2, char3), lcs(char1, char2[:len2-1], char3), lcs(char1, char2, char3[:len3-1]))
        
    return dp[len1][len2][len3]

print(lcs(temp1, temp2, temp3))