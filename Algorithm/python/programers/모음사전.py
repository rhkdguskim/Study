words = ['', 'A', 'E', 'I', 'O', 'U']
def solution(word):
    return sorted(set([w1+w2+w3+w4+w5 for w1 in words for w2 in words for w3 in words for w4 in words for w5 in words])).index(word)
