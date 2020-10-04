def best(C, items):         #currently knapsack 0-1
    n = len(items)
    keep = [[0 for x in range(C+1)] for x in range(n+1)] #2D way for holding decisions to keep or not

    for i in range(n + 1):
        
        wtlast, valast,clast = items[i-1]
        for w in range(C+1):
            if i==0 or w==0: keep[i][w] = 0
            elif wtlast < w:
                keep[i][w] = max(valast + keep[i-1][w-wtlast], keep[i-1][w])
                #wt, val, c = items[i]
                #items.append((wt, val, c-1))
                #n+=1
            else:
               keep[i][w] = keep[i-1][w]
    
    return (keep[n][C])




print(best(3, [(2, 4, 2), (3, 5, 3)]))