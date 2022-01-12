import functools
import operator

alIst=[1,2,3,4,5,6,7,8,9]

red1 = functools.reduce(lambda a,b: a+b,alIst)
red2 = functools.reduce(lambda a,b: a if a > b else b,alIst)
red3 = functools.reduce(operator.add,alIst)

print(red1)#45
print(red2)
print(red3)#45