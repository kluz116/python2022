def fun():
    print('Welcome To Python')

fun()

def EvenOrOdd(x):
    if x%2==0:
        return 'Even'
    else:
        return 'Odd'

print(EvenOrOdd(3))

def DefaultFun(x, y=3):
    print('X',x)
    print('Y',y)

DefaultFun(5)


def GetName(firstname,Lastname):
    print(firstname='Allan ')