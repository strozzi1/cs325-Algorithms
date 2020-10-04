from heapq import heappush, heappop, heapify
def nbest(ABs):    # no need to pass in k or n
    def trypush(i, p, q):  # push pair (A_i,p, B_i,q) if possible
        A, B = ABs[i] # A_i, B_i
        if p < n and q < n and (i, p, q) not in used:
            heappush(h, (A[p] + B[q] , i, p, q, (A[p],B[q])))
            used.add((i, p, q))
    k, n = len(ABs), len(ABs[0][0])
    h, used = [ ], set()                 # initialize
    for i in range(k):  # NEED TO OPTIMIZE
        trypush(i, 0, 0)

    for _ in range(n): 
        _, i, p, q, pair = heappop(h)
        yield pair     # return the next pair (in a lazy list)
        trypush(i, p+1, q)
        trypush(i, p, q+1)


print(list(nbest([([5,6,10,14],[3,5,10,14]),([2,7,9,11],[3,8,12,16]),([1,3,8,10],[5,9,10,11]),([1,2,3,5],[3,4,9,10]),([4,5,9,10],[2,4,6,11]),([4,6,10,13],[2,3,5,9]),([3,7,10,12],[1,2,5,10]),([5,9,14,15],[4,8,13,14])])))
