def decorator_fun(func):

    def wrapper_func(name):
        print('This is going to be decorated')
        func(name)
        print('Done with getting decorated')
    return wrapper_func

@decorator_fun
def sayHello(name):
    print(f'Saying Hi To {name}')

sayHello('Allan Musembya')

