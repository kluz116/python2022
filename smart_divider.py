def smart_divider(func):
    def inner_wrapper(a,b):
        if a == 0 or b==0:
            print(f'Whoops, {a}  can not be zeor or {b} can not be zero')
            
        return f'The division results  is {func(a,b)}' 
    return inner_wrapper

@smart_divider
def divide_num(a,b):
    return (a/b)

print(divide_num(10,4))