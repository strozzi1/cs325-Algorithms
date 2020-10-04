from collections import defaultdict
from heapq import *
    


allowed = set(['AU', 'UA', 'CG', 'GC', 'GU', 'UG'])
def best(rna):   #teacher provided in class
    
    def _best(i, j):
        if (i, j) in opt:
            return opt[i, j]
        curr = -1
        for k in range(i, j):
            if _best(i,k) + _best(k+1, j) > curr:
                curr = max(curr, _best(i,k)+ _best(k+1, j))
                back[i, j] = k
            #curr = max(curr, _best(i,k)+ _best(k+1, j))
        if rna[i] + rna[j] in allowed:
            if _best(i+1, j-1) + 1 > curr:
                curr = _best(i+1, j-1) +1
                back[i, j] =  -1
            #curr = max(curr, _best(i+1, j-1) +1)
        opt[i,j] = curr
        return curr
    

    def solution(i, j):
        if i == j: #singleton
            return "."
        if i > j: #empty
            return ""
        k = back[i, j]
        if k == -1:
            return "(%s)" % solution(i+1, j-1)
        else:
            return solution(i, k) + solution(k+1, j)

    opt = defaultdict(int)
    back = {}
    n = len(rna)
    for i in range(n):
        opt[i, i] = 0
        opt[i, i-1] = 0

    return _best(0, n-1), solution(0, n-1)



def total(rna):
    def _total(i, j):
        if(i, j) in opt:
            return opt[i,j]

        counter = 0
        for k in range(i, j):
            if rna[j] + rna[k] in allowed:
                counter += _total(i, k-1) * _total(k+1, j-1)

        counter += _total(i, j-1)
        opt[i,j] = counter

        return counter
    opt = defaultdict(int)
    n = len(rna)

    for i in range(n):
        opt[i, i] = 1
        opt[i, i-1] = 1

    return _total(0, n-1)

    
    return 0

def kbest(rna, k):
    def _kbest(i,j):
        def trypush_binary(s,p,q):
            if p < len(topk[i,s]) and q < len(topk[s+1,j]) and (s,p,q) not in visited:
                heappush(h,(- (topk[i,s][p][0] + topk[s+1,j][q][0]),(s,p,q)))
                visited.add((s,p,q))

        def trypush_unary(p):
            if p < len(topk[i+1,j-1]):
                heappush(h, (- (topk[i+1,j-1][p][0]+1),(p,)))

        if (i,j) in topk:
            return topk[i,j]

        if i==j:
            topk[i,j] = [(0,'.')]
            return
        elif j == i-1:
            topk[i,i-1] = [(0,'')]
            return

        h = []
        visited = set()
        for s in range(i,j):
            _kbest(i,s)
            _kbest(s+1,j)
            trypush_binary(s, 0,0)

        if rna[i]+rna[j] in allowed:
            _kbest(i+1,j-1)
            trypush_unary(0)

        found = 0
        while found < k:
            if h == []:
                print("not enough pushed")
                break
            score, indices = heappop(h)
            # print(past)
            try:
                s,p,q = indices
                ans = (-score, "%s%s" % (topk[i,s][p][1],topk[s+1,j][q][1]))

                if ans not in topk[i, j]:
                    topk[i, j].append(ans)
                    found += 1
                    # past[i, j, p, q] = ans

                trypush_binary(s,p+1,q)
                trypush_binary(s,p,q+1)
            except:
                p = indices[0]
                ans = (-score, "(%s)" % topk[i+1,j-1][p][1])
                # print(ans)

                if ans not in topk[i,j]:
                    topk[i, j].append(ans)
                    found += 1
                    # past[i, j, p] = ans

                trypush_unary(p+1)

    topk = defaultdict(list)
    past = {}
    n = len(rna)
    _kbest(0,n-1)
  
    return _kbest(0,n-1)


    return 0





if __name__ == "__main__":
    #best("ACGGUCGAC")
    print(best('AACCGCUGUGUCAAGCCCAUCCUGCCUUGUU'))