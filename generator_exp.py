x = [x **2 for x in range(1,10) if x%2==0]
y = (x **2 for x in range(1,10) if x%2 ==0)
print(x)
print(next(y))
