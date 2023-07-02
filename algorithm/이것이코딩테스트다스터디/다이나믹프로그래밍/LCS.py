# https://www.acmicpc.net/problem/9251
# 부분 수열(Subsequence)이란, x의 몇몇 원소들을 제거하거나 그러지 않고 남은 원소들이 원래 순서를 유지하여 얻을 수 있는 새로운 수열을 말합니다.
str1 = str(input())
str2 = str(input())
length1 = len(str1)
length2 = len(str2)

def LCS(i,j):
    if length1 > i >= 0 and length2 > j >=0:
        if str1[i] == str2[j]:
            return LCS(i-1,j-1) + 1
        else :
            return max(LCS(i-1, j), LCS(i, j-1))
    else:
        return 0
    
print(LCS(length1-1, length2-1))