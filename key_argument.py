def getSum(*args):
    count =0
    for i in args:
        count+=i
    return count

print(getSum(1,2,3,4,5))

def getName(**args):
    for key,value in args.items():
        print('{} = {}'.format(key,value))

getName(a='allan',b='Musembya',c='Jolly')

student = {'Name':'Allan Musembya','age':45,'std_class':'S5'}
