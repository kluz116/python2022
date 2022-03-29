def decorator_allan(func):
    def inner(**kwargs):
        func(**kwargs)
    return inner


@decorator_allan
def getItems(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} {value}')




