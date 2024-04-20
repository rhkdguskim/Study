# https://www.acmicpc.net/problem/11000
import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())

edu = []
for _ in range(N):
    edu.append(list(map(int, input().split())))
    
edu.sort(key=lambda x:(x[0], x[1] - x[0]))

end_times = [edu[0][1]]

for s, e in edu[1:]:
    flag = False
    for i in range(len(end_times)):
        if s >= end_times[i]:
            end_times[i] = e
            flag = True
            break
    
    if not flag:
        end_times.append(e)
        
print(len(end_times))
#print(end_times)