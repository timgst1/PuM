def fib(x):
    if x <= 1:
        return x

    else:
        return fib(x-1)+fib(x-2)


def fibiterate(x):
    fibone = 0
    fibtwo = 1 

    for i in range(x):
        newfib = fibone + fibtwo
        fibone = fibtwo
        fibtwo = newfib
    
    return newfib
