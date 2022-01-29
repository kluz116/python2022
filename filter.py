aList = [2,3,4,5,6,7]

res = filter(lambda x:x%2==0,aList)

print(list(res))#[2, 4, 6]

res1 = filter(lambda x:x%2!=0,aList)

print(list(res1))