class Trie():
    def __init__(self):
        self.child = {}
        self.length = {}
        
    def push(self, word):
        node = self
        while len(word) > 0:
            node.length[len(word)] = node.length.get((len(word)), 0) + 1
            if word[0] not in node.child:
                node.child[word[0]] = Trie()
            node = node.child.get(word[0])
            word = word[1:]
            
    def search(self, word):
        node = self
        while len(word) > 0:
            if word[0] == '?':
                return node.length.get(len(word), 0)
            
            if word[0] not in node.child:
                return 0
            
            node = node.child[word[0]]
            word = word[1:]

def solution(words, queries):
    t1 = Trie()
    t2 = Trie()
    for word in words:
        t1.push(word)
        t2.push(word[::-1])
    
    answer = []
    for query in queries:
        if query[0] == '?':
            answer.append(t2.search(query[::-1]))
        else:
            answer.append(t1.search(query))
            
    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))