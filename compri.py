import itertools


res = [x for x in range(1,10) if x%2==0]
print(res)

list_num = [1,2,3,4,5,6]
iterable_obj = iter(list_num)
print(next(iterable_obj))
print(next(iterable_obj))