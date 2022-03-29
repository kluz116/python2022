def make_pretty(func):
    def wrapper_func():
        print('Getting Decorated')
        func()
    return wrapper_func

def ordinary_func():
    print('This is an ordinary function')


res = make_pretty(ordinary_func)
res()
