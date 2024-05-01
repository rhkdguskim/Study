# https://school.programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    temp = set(list(skill))

    # 선행스킬만 필터링 하여 리턴한다.
    def f(s):
        return ''.join([s[c] for c in range(len(s)) if s[c] in temp])

    # 길이만큼 비교하고 같은 문자만 남긴다.
    def f2(s):
        t = skill[:len(s)]
        return t == s

    # 2개의 필터를 거친 개수를 리턴한다.
    return len(list(filter(f2, map(f, skill_trees))))

