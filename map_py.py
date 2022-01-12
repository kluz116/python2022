def getSum(x):
    return x+x

print(list(map(getSum,(1,2,3,4,5,6))))

w= list(map(lambda y: y+y,(1,2,3,4,5,6) ))
print(w)

#Using a map function to add two numbers
a = [1,2,3,4]
b=  [2,3,4,6]

results = map(lambda x,y : x+y,a,b)
print(list(results))

#Adding two numbers using a function
def getAdd(x,y):
    return x + y
res = map(getAdd,a,b)
print(list(res))


