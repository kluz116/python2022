a = [1,2,3]
b = ['Alan','James','Keith']

x = list(zip(a,b))
print(x)

for val1, val2 in zip(a,b):
    print(val1,val2)