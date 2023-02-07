def demo(x):
    return lambda a:a*x

d=demo(6)
print(d(11))


