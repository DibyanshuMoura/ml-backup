def sum(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

def sub(*args):
    sub = 0
    for arg in args:
        sub -= arg
    return sub

def mul(*args):
    mul = 1
    for arg in args:
        mul *= arg
    return mul

def div(a, b):
    return a / b
