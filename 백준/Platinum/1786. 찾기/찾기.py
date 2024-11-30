import sys
input = sys.stdin.readline

def get_pi(w):
    l, j, pi = len(w), 0, [0 for _ in range(len(w))]
    for i in range(1, l):
        while j > 0 and w[i] != w[j]: 
            j = pi[j-1]
        
        if w[i] == w[j]: 
            j += 1
            pi[i] = j
    
    return pi

def kmp(s, p):
    ans = []
    j, pi, l = 0, get_pi(p), len(p)
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]: 
            j = pi[j-1]
        
        if s[i] == p[j]:
            if j == l-1:
                ans.append(i-l+1)
                j = pi[j]
            else:
                j += 1
    return ans

ans = kmp(input().rstrip(), input().rstrip())

print(len(ans))
print(" ".join(map(str, map(lambda x:x+1,ans))))