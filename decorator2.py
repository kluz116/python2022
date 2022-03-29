def smart_divider(func):
    def inner(a,b):
        if b == 0:
            print(f'Whoops {b} can not be Zero')
            return
        return func(a,b)
    return inner


@smart_divider
def divide(a,b):
    print(f'The division of {a} and {b} is {a/b}')

    
divide(12,6)


