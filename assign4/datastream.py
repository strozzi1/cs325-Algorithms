import heapq
#can use heappop, heappush, heapreplace, and heapify
#note: sometimes you can "negate" the values to simiulate a max heap using a min heap. ie..multiply all vals by -1 to make it a max heap 

def ksmallest(k, a):
    if(k>len(a)): k = len(a)        #sometimes k is greater than the length of the array
    heap=a[0:k]
    
    for i in range(k):              
        heap[i] *= -1
    heapq.heapify(heap)             #now have what is in effect a max heap
    #print(heap)
    arraylen = len(a)
    for i in a[k:]:
        if -i > heap[0]:
            heapq.heapreplace(heap, -i)
            #heapq.heapify(heap)

    #print(heap)
    sortedk = [0] * k               #initialize new sorted version of the
    
    j = k - 1 
    while j >=0:
        sortedk[j] = heapq.heappop(heap) *-1
        j -= 1
    return sortedk


    

#print(ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7])) #[2, 3, 5, 7]
#print(ksmallest(3, range(1000000, 0, -1))) #[1, 2, 3]