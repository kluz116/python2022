
aList=[1,2,3,4,5,6,7,8,9]
x= list(map(lambda x:x*2,aList))
print(x)

print([2*x for x in aList])

print(list(filter(lambda x: x%2==0,aList)))
print([ x for x in aList if x%2==0])