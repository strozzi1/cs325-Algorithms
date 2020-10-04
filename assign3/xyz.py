def find(a):
    final = [ ]
    for i, x in enumerate (a[:-1]):
        for y in a[i+1:]:
            if x+y in a: 
                #print(x, y, x+y)
                #print("[",x,y,x+y,"]")
                truple = (x,y,x+y)
                final.append(truple)
                #final.append([x, y, x+y])
    #print final
    return(final)
            
#find([1,4,2,3,5])