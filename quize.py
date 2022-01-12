aList = [1, 2, 3, 4, 5, 6, 7]
pow2 =  [2 * x for x in aList]
#print(pow2)


def getPow(x):
    return x * 2

#print(getPow(2))

y = map(getPow,aList)
print(list(map(getPow,aList)))
print(list(map(lambda x: x*2,aList)))