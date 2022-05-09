def outerfunc(func):
    print('This is an outer function')
    def inner_func():
        print('This is an Inner function')
        func()
    return inner_func

@outerfunc
def getName():
    print('Am Allan Musembya')

getName()