

def best(C, items):
    n = len(items)
    keep = [0 for x in range(C+1)] #2D way for holding decisions to keep or not
    kept = [0] * n

    for j in range(0, C+1):
        for i in range(n):
            wi, vi = items[i]
            if wi <= j:
                
                keep[j] = max(keep[j], keep[j - wi] + vi)   #max(keep[w-wi] + vi, of all item i)

    print(keep)
    return (keep[C], kept)
        





#for i in range(1,3): print i
print(best(3, [(2, 4), (3, 5)]))
#print(best(92, [(8, 9), (9, 10), (10, 12), (5, 6)]))
