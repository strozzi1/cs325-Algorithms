import heapq
import math
def kmergesort(a, k):
    arrays = split(a, k)
    heap = [  ] 
    ptrs = [ 1 ] * k
    result = [ ]
    #print(arrays)
    for i in range(k):                  #where i is each array
        arrays[i]=mergesort(arrays[i])  # arrays are sorted
        
    #print(arrays)
    #heapq.heapify(heap)
    for i, currarr in enumerate(arrays):
        heapq.heappush(heap, (currarr[0], i))

    #print(heap)
    for i in range(len(a)):
        currmin, aidx = heap[0]
        result.append(currmin)
        if ptrs[aidx] < len(arrays[aidx]):
            heapq.heapreplace(heap, (arrays[aidx][ptrs[aidx]], aidx))
            ptrs[aidx] +=1
        else:
            heapq.heapreplace(heap, (math.inf, -1))
            #heapq.heapify(heap)

        
    

    print(result)
    return result
    




#takes list and turns it into a list of n evenly distributed lists
def split(a, n):
    k, m = divmod(len(a), n)
    return [ a [ i * k + min(i,m):( i + 1 ) * k + min( i + 1, m )] for i in range(n)]



def mergesort(arr):
    arrlen = len(arr)
    if arrlen > 1:
        mid = arrlen//2
        left = arr[ :mid]
        right = arr[ mid: ]
        mergesort(left )
        mergesort(right )

        i=0
        j=0
        k=0


        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] =left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            arr[k]=left[i]
            i+=1
            k+=1

        while j < len(right):
            arr[k]=right[j]
            j+=1
            k+=1
        
        return(arr)



kmergesort([4,1,5,2,6,3,7,0], 3) #[0,1,2,3,4,5,6,7]