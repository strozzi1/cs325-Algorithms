def qsort(a):
    if a == [ ]:
        return [ ]
    else:
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        return qsort(left) + [pivot] + qsort(right)
    
def sort(b):
    if b == [ ]:
        return [ ]
    else:
        pivot = b[0]
        left = [x for x in b if x < pivot]
        right = [x for x in b[1:] if x >= pivot]
        return [sort(left)] + [pivot] + [sort(right)]

def search(bst, a):
    for x in bst:
        if a == x:
            return True
    return False


def insert(tree, b):
   r = _search(tree, b)
   if r==[]:
       r += [[], b, []]









    

