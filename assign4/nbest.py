import random
import heapq

def both(val):
    return val[0]+val[1]


def nbesta(a, b):
    pairs = [ ]
    for i in a:
        for j in b:
            pairs.append( (i, j) )

    #print(pairs)
    pairs.sort(key=both)
    return pairs[:4]





def nbestb(a, b):
    allpairs = [ ]
    sums = [ ]
    result = [ ]
    for i in a:
        for j in b:
            allpairs.append( (i, j) )
    for i,pair in enumerate(allpairs):
        sums.append( (pair[0]+pair[1], i ))
    #print(sums)

    for i in range(1, len(a)+1):
        s, idx = qselect(i, sums)
        result.append(allpairs[idx])
        
    return(result)

def nbestc(a, b):
    allpairs = [ ]
    res = [ ]
    for i in a:
        for j in b:
            allpairs.append( (i+j,(i, j)) )

    heapq.heapify(allpairs)
    #print(allpairs)
    for i in range(len(a)):
        new=(heapq.heappop(allpairs))
        res.append(new[1])
    return(res)


    



def qselect(k,a):
    if a == [] or k>len(a) or k==0:
        return []
    else:
        i=random.randint(0,len(a)-1)
        a[0],a[i]=a[i],a[0]
        pivot=a[0]
        left = [x for x in a if x < pivot ]


        splitP=len(left)
        if splitP==k-1:
            return pivot
        
        elif splitP>k-1:
            return qselect(k,left)
        
        else:
            right = [x for x in a[1:] if x >= pivot]
            return qselect(k-(splitP+1),right)









#a, b = [4, 1, 5, 3], [2, 6, 3, 4]
#print(nbesta(a, b))
#print(nbestb(a, b))
#print(nbestc(a, b))