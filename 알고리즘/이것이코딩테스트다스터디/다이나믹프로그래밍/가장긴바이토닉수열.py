# https://www.acmicpc.net/problem/11054
from bisect import bisect_left
N = int(input())
arr = list(map(int, input().split()))

maxvalue = 0
for i in range(N):
    leftarr = arr[:i+1]
    rightarr = arr[i:]
    
    
    temp = [leftarr[0]]
    for j in range(len(leftarr)):
        if leftarr[j] > temp[-1]:
            temp.append(leftarr[j])
        else:
            idx = bisect_left(temp, leftarr[j])
            temp[idx] = leftarr[j]
            
    rightarr.reverse()
    temp2 = [rightarr[0]]
    for j in range(len(rightarr)):
        if rightarr[j] > temp2[-1]:
            temp2.append(rightarr[j])
        else:
            idx = bisect_left(temp2, rightarr[j])
            temp2[idx] = rightarr[j]
            
    maxvalue = max(maxvalue, len(temp)+len(temp2) -1)

print(maxvalue)