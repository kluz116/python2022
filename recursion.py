def recursion_decorator(func):
    def inner(n):
        if n == 0:
            return 0
        return func(n)
    return inner
        

@recursion_decorator
def recursion_sum(n):
    return n + recursion_sum(n-1)


print(recursion_sum(10))