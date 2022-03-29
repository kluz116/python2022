def operator(func_passed):
    def inner(a,b):
        print('Going to do some funny crap in here')
        func_passed(a,b)
    return inner

@operator
def sum(a,b):
    print(a+b)


sum(3,4)

