from bisect import *
def find(a, x, k):    ##params: array, comparison number, number of near numbers
    final =[ ]
  ##find where to put the two pointers, one going left, one going right
    left = bisect_left(a, x)-1
    right = left+1
    print(a[left], a[right])
    for i in range(k):
        if right >=len(a):
            for j in range(k-i):
                final.insert(0, a[left])
                left-=1
            return final
        elif left < 0:
            for j in range(k - i):
                final.append(a[right])
                right+=1
            return final
        
        l = abs(a[left] - x)        #find the diff
        r = abs(a[right] - x)
        if r < l and right <= len(a):
            final.append(a[right])
            right+=1
        else:
            final.insert(0, a[left])
            left-=1



    #print(final)
    return(final)



    



