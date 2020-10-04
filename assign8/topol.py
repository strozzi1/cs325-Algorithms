from collections import defaultdict

def order(n, edges):
    adjlist = defaultdict(list)
    indegree = defaultdict(int)
    result = [ ]
    
    for u, v in edges:
        adjlist[u].append(v)
        indegree[v] += 1
    
    
    stack = []

    for u in range(n):
        if indegree[u] == 0:
            stack.append(u)
    while stack != []:
        u = stack.pop(0)
        #yield u
        result.append(u)
        for v in adjlist[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                stack.append(v)

    return result



print(order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))