# https://school.programmers.co.kr/learn/courses/30/lessons/340211
from collections import defaultdict

def solution(points, routes):
    path = defaultdict(int)
    
    def point(p):
        return points[p-1]
    
    def next(r, c, next):
        cy, cx = r, c
        ny, nx = points[next-1]
        
        if cy != ny:
            if cy > ny:
                return (r-1, c)
            else:
                return (r+1, c)
        else:
            if cx > nx:
                return (r, c-1)
            else:
                return (r, c+1)
    

    for route in routes:
        cnt = 0
        cy, cx = point(route[0])
        path[(cy, cx, cnt)] += 1
        for i in range(len(route)-1):
            n = route[i+1]
            ny, nx = point(n)
            while cy != ny or cx != nx:
                cy, cx = next(cy, cx, n)
                cnt += 1
                path[(cy, cx, cnt)] += 1
    
    answer = 0
    for _, v in path.items():
        if v >= 2:
            answer += 1   
    
    return answer