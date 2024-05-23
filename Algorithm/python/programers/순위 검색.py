# https://school.programmers.co.kr/learn/courses/30/lessons/72412
def solution(info, query):
    def bisect_left(arr, score):
        start = 0
        end = len(arr)
        
        while start < end:
            mid = (start + end) // 2
            if arr[mid] < score:
                start = mid + 1
            else:
                end = mid

        return start
    
    class Node():
        def __init__(self) -> None:
            self.child = {}
            self.data = []
        
    class Trie():
        def __init__(self) -> None:
            self.head = Node()
            
        def insert(self, info):
            current_node = self.head
            n = len(info)
            for i in range(n-1):
                if info[i] not in current_node.child:
                    current_node.child[info[i]] = Node()
                
                current_node = current_node.child[info[i]]
            
            scores = current_node.data
            score = int(info[-1])
            idx = bisect_left(scores, score)
            scores.insert(idx, score)
            
        
        def search(self, query):
            current_node = [self.head]
            n = len(query)
            
            for i in range(n-1):
                next_current_node = []
                # '-'가 등장할 경우 모든 child들을 다음 검색할 노드에 넣는다.
                if query[i] == '-':
                    for node in current_node:
                        for key in node.child.keys():
                            next_current_node.append(node.child[key])
                else:
                    for node in current_node:
                        # query[i]에 존재하는 노드만 추가한다.
                        if query[i] in node.child:
                            next_current_node.append(node.child[query[i]])
                
                current_node = next_current_node
            
            cnt = 0
            score = int(query[-1])
            # 마지막 노드를 순회하면서 score보다 큰 값을 찾는다.
            for node in current_node:
                scores = node.data
                n = len(scores)
                l = bisect_left(scores, score)
                cnt += n - l
                
            return cnt
                    
    trie = Trie()
    for i in info:
        i = i.split(' ')
        trie.insert(i)
    
    answer = []
    for q in query:
        q = q.replace(" and", "").split(' ')
        answer.append(trie.search(q))
        
    return answer