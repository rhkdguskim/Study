# https://school.programmers.co.kr/learn/courses/30/lessons/12983

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.end_of_word = True


def solution(strs, t):
    trie = Trie()
    for s in strs:
        trie.insert(s)

    n = len(t)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(n):
        if dp[i] == float('inf'):
            continue
        current = trie.root
        for j in range(i, n):
            if t[j] not in current.children:
                break
            current = current.children[t[j]]
            if current.end_of_word:
                dp[j + 1] = min(dp[j + 1], dp[i] + 1)

    return dp[n] if dp[n] != float('inf') else -1
