def longest(arr):
    
    longpath, depth = inorder(arr)
    return longpath-1  # tuple(longest path)

def inorder(bst):
    
    if bst == []:
        return 0, 0 
    left, ldepth = inorder(bst[0])
    right, rdepth = inorder(bst[2])

    #path = max(path, left + right)
    path = max(left, right)

    return max( 1 + ldepth + rdepth, path), (max(ldepth, rdepth)+1)


