# https://www.acmicpc.net/problem/3649

import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input())
        n = int(input())
        lego = []
        for _ in range(n):
            lego.append(int(input()))
            
        lego.sort()
        max_cost = -1
        l1, l2 = -1, -1
        checker = x * (10**7)
        for i in range(n):
            start = i+1
            end = n-1
            while end >= start:
                mid = (start+end)//2
                cost = lego[i] + lego[mid]
                if cost == checker:
                    if abs(lego[i] - lego[mid]) > max_cost:
                        max_cost = abs(lego[i] - lego[mid])
                        l1, l2 = i, mid
                        
                    break
                elif cost > checker:
                    end = mid - 1
                else:
                    start = mid + 1
        
        if l1 != -1 and l2 != -1:
            print("yes", lego[l1], lego[l2])
        else:
            print("danger")
    except:
        break