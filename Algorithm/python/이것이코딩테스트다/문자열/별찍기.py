# https://www.acmicpc.net/problem/2447
N = int(input())

def drawStar(N):
    if N == 1:
        return '*'
    
    stars = drawStar(N//3)
    
    L = []
    for star in stars:
        L.append(star*3)
    for star in stars:
        L.append(star + ' '* (N//3) + star)
    for star in stars:
        L.append(star*3)
        
    return L


for star in drawStar(N):
    print(star)
    
        