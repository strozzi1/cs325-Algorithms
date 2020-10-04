from heapdict import heapdict
from collections import defaultdict


def shortest(target, edges):
    def solution(v):
        if v not in bt:
            return[v]
        return solution(bt[v]) + [v]
    if edges == [ ]: return None
    #d = heapdict()
    d = defaultdict(lambda: float("inf"))
    pq = heapdict()
    bt = defaultdict(None)
    seen = defaultdict(int)
    adjlist = defaultdict(list)
    for v1, v2, w in edges:
        adjlist[v1].append((v2, w))
        adjlist[v2].append((v1, w))


    d[0] = 0
    path = [ ]
    #pq[0] = edges[0]
    pq[0] = 0
    while pq:
        u, weight = pq.popitem()
        #path.append(u)
        if u not in seen:
            seen[u] = weight
            if u == target-1: break
            for v, w in adjlist[u]:
                if v not in seen:
                    if(d[v]> d[u]+w):
                        pq[v] = d[v] = (d[u] + w)
                        bt[v] = u
    
    
    if target-1 not in bt or bt[target-1] is None:
        return None
    else:
        bt[target] = target-1
        path = solution(bt[target])
        return (weight, path)




#shortest(8, [(0,4,2), (2,3,1), (2,5,1), (3,6,2), (3,4,1),(2,4,1), (2,7,1)])
#print(shortest(4, [(0,1,1), (2,3,1)])) #== None



        