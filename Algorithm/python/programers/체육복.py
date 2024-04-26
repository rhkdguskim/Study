def solution(n, lost, reserve):
    reserve = set(reserve)

    new_lost = []
    for l in lost:
        if l in reserve:
            reserve.remove(l)
        else:
            new_lost.append(l)

    new_lost.sort()


    answer = n - len(new_lost)

    for l in new_lost:
        if l-1 in reserve:
            answer += 1
            reserve.remove(l-1)
            continue
        if l+1 in reserve:
            answer += 1
            reserve.remove(l+1)

    return answer