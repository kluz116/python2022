def sum(a,b):
    def inner():
        return a+b
    return inner

res = sum(1,5)
print(res())