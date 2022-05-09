def funcs(func):
    def func(a,b):
        if a==0 and b== 0:
            return f'Value a can not be {a} or b can not be {b}'
        else:
            return a+b

    return func

@funcs
def getAdd(a,b):
    return a+b

print(getAdd(8,9))

