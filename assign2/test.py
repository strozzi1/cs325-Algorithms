from msort import *
from inversions import *
from longest import *
testarr=[4,2,3,5,6,1,9,8]
mid =len(testarr)//2
arr1=mergesort(testarr)
print "mergesort: ",arr1

#for x in testarr[0:mid]:
#    print("l: ", x)

#for x in testarr[mid:]:
#    print("r: ", x)

testarr2=[4,2,3,5,6,1,9,8]
print "inversions(4): ",num_inversions([4, 1, 3, 2])# - 4
print "inversions(3): ",num_inversions([2, 4, 1, 3])# - 3

print "longest(0): ",longest([[], 1, []])
print "longest(5): ",longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]])
print "longest(2): ",longest([[[], 1, []], 2, [[], 3, []]])