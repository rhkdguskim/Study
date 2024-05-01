# https://school.programmers.co.kr/learn/courses/30/lessons/62048

def solution(w,h):
    # w > h
    w, h = max(w, h), min(w, h)

    def gcd(w, h):
        if h == 0:
            return w
        else:
            return gcd(h, w % h)

    g = gcd(w, h)

    ww = w // g
    hh = h // g

    cut = ww*hh - (ww-1)*(hh-1)

    return w*h - cut*g