def qselect(a, lst):

    pivot = lst[0]
    left = [x for x in lst if x < pivot]
    right = [x for x in lst[1:] if x >= pivot]
    
    left_len = len(left)
    right_len = len(lst)-len(right)

    if left_len > a-1:
        return qselect(a, left)
    elif a-1 >= right_len:
        return qselect((a-1 )-left_len, right)
    else:
        return pivot

        



def betterselect(a, lst):
    #watch beginning of lecture vid 11 minutes in or so
