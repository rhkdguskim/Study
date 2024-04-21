def solution(citations):
    citations.sort(reverse=True)
    answer = 0
    for i, v in enumerate(citations, start=1):
        answer = max(min(i, v), answer)

    return answer