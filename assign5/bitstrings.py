def num_no(n, no_list=None):             #repurpose of fibonacci
    if no_list is None: no_list={0:1, 1:2}
    if n not in no_list:
        no_list[n] = num_no(n-1) + num_no(n-2)
    return no_list[n]



def num_yes(n):
    return 2**n - num_no(n)
