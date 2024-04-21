def solution(sizes):
    a=[]
    b=[]
    for i in sizes:
        a.append(max(i))
        b.append(min(i))

    return max(a)*max(b)