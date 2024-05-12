def solution(a, edges):
    if sum(a) != 0:
        return -1
    
    n = len(a)
    adj = [set() for _ in range(n)]
    
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    
    leaf_nodes = [i for i in range(n) if len(adj[i]) == 1]
    cnt = 0
    
    while leaf_nodes:
        new_leaf_nodes = []
        for leaf in leaf_nodes:
            if len(adj[leaf]) == 0:
                continue
            
            parent = adj[leaf].pop()
            cnt += abs(a[leaf])
            a[parent] += a[leaf]
            a[leaf] = 0
            adj[parent].remove(leaf)
            if len(adj[parent]) == 1:
                new_leaf_nodes.append(parent)
        leaf_nodes = new_leaf_nodes
    
    return cnt
