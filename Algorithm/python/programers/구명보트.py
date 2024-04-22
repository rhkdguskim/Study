def solution(people, limit):
    people.sort()
    l_p = 0
    r_p = len(people) - 1

    answer = 0

    while r_p >= l_p:
        if r_p == l_p:
            r_p -= 1
            answer += 1
            break

        light = people[l_p]
        heavy = people[r_p]

        if limit >= light + heavy:
            r_p -= 1
            l_p += 1
            answer += 1
        else:
            r_p -= 1
            answer += 1

    return answer

print(solution([50, 50, 70, 80], 100))

# 50 50 70 80
# 50 70 80