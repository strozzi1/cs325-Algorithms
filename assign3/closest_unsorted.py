import random
from random import randint
def find(a, x, k):    ##params: array, comparison number, number of near numbers
    diffarray = [abs(y-x) for y in a] #array of the difference between each element and x

    ksmallest = quickselect(k, diffarray)
    #print("k: ", ksmallest)
    #return pivot
    index = [g for g,j in enumerate(diffarray) if j < ksmallest]

    for i,g in enumerate(diffarray, 0):
        if g == ksmallest:
            #print(i, g)
            index.append(i)
    #print(index)
    index.sort()
    final=[ ] #initialize final
    for i in range(0,len(index)):
        final.append(a[index[i]])
    #print( final)
    return final


def quickselect(k,a):   #from class returns number at sorted index
    if a == [] or k>len(a) or k==0:
        return []
    else:
        #i=random.randint(0,len(a)-1)
        #a[0],a[i]=a[i],a[0]
        pivot=a[0]
        left = [x for x in a if x < pivot ]


        splitP=len(left)
        if splitP==k-1:
            return pivot
        
        elif splitP>k-1:
            return quickselect(k,left)
        
        else:
            right = [x for x in a[1:] if x >= pivot]
            return quickselect(k-(splitP+1),right)