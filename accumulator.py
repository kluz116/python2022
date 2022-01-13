import functools
import itertools


alIst=[1,2,3,4,5,6,7,8,9]
acc1 = itertools.accumulate(alIst, lambda x,y:x+y)

print(list(acc1))