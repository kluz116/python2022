
def create_stack():
    stack = []
    return stack

def check_empyty(stack):
    return len(stack)==0
        
def push(stack:list,item:int):
    stack.append(item)
    print(f'The Item pushed is : {item}')

def pop(stack):
    if check_empyty(stack):
        return 'The stack is empty'
    return stack.pop()

stack = create_stack()
push(stack,23)
push(stack,30)
push(stack,40)
push(stack,50)
push(stack,60)

print(stack)
pop(stack)
print(stack)







