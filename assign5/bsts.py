#geeksforgeeks.org was my ultimate resources

def bsts(n, law=None):
    li = [0] * (n+1)

    li[0],li[1] = 1,1
    for i in range(2, n+1):
        for j in range(1, i+1):
            #law[i]=(law[j-1] * law[i-j])+law[i]
            li[i] += li[j-1]*li[i-j]
       
    return li[n]



