def my_generator():
    n = 1
    yield n
    n+=1
    yield n
    n+=1
    yield n

x = my_generator()
print(next(x))
print(next(x))
print(next(x))


for gen in x:
    print(gen)
