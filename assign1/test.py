from qsort import *
from qselect import *
a = qsort([2, 3, 19, 4, 7, 10])

print(a)

lst = [4,2,6,3,5,7,1,9]
print("qselect(2, [4, 3, 1, 6]")
b = qselect(2, [4, 3, 1, 6])

print b

c =qselect(4, [11, 2, 8, 3])
print(c)

bst = sort([4,2,6,3,5,7,1,9])
print(bst)

bool1 = search([5,6,1,3,2], 1)
print bool1

inserted = insert([4,2,6,3,5,7,1,9], 6.5)
print(inserted)
