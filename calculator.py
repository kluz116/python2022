from secrets import choice


add = lambda a,b : a+b
sub = lambda a,b : a-b
mul = lambda a,b : a*b
print('---------------------------------')
print('Select the action from below: ')
choice = input('Add (1), Sub (2), Mul (3) : ')

a = int(input('Put one number here : '))
b = int(input('Put two number here : '))

if choice =='1':
    print(f'The Sum of {a} and {b} is {add(a,b)}')
elif choice == '2':
    print(f'The Sub of {a} and {b} is {sub(a,b)}')
elif choice == '3':
    print(f'The Multplication of {a} and {b} is {mul(a,b)}')
    