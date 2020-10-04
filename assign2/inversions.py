def num_inversions(arr):
    arrlen = len(arr)

    if arrlen <= 1:
        return 0

    mid = arrlen//2
    left = arr[ :mid]
    right = arr[ mid: ]
    li=num_inversions(left)
    ri=num_inversions(right)

    lri=mergecount(left, right)
    #print "left invs: ", li, "\nright invs: ", ri
    #print "mergeinvs: ", lri

    inversions = lri
    return inversions

def mergecount(left, right):
    i=0
    j=0
    k=0
    invs=0
    arr = [ ] #* (len(left) + len(right) )

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            #arr[k] =left[i]
            arr.append(left[i])
            i+=1
        else:
            #arr[k] = right[j]
            arr.append(right[j])
            j+=1
            invs+=(len(left)-i)
        #k+=1
    arr+=left[i:]
    arr+=right[j:]

    
    return(invs)