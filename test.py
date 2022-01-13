import functools
import operator
import itertools
aList = [2,3,4,5,6,7]

res = map(lambda x: x*2,aList)
print(list(res))

red = functools.reduce(lambda x,y : x+y,aList)
print(red)

red1 = functools.reduce(operator.add, aList)

print(red1)

red2 = itertools.accumulate(aList, lambda x,y: x+y)

print(list(red2))