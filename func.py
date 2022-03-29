def decorator_func(func):
    def inner(*args):
        return func(*args)
    return inner


@decorator_func
def sum(*args):
    count = 0
    for i in args:
        count += i
    return count

print(sum(1,2,3,4,5,6,7,8,9))
