def simple_function():
    x = 10
    return x

def complex_function(a, b):
    if a > b:
        for i in range(b):
            if i % 2 == 0:
                try:
                    x = 1 / i
                except ZeroDivisionError:
                    x = 0
    else:
        while a < b:
            a += 1
            if a == b:
                break

def long_function():
    for i in range(10):
        print(i)
    # Some comment here
    # Another comment line
    for j in range(20):
        print(j)

def bool_op_function():
    if (a and b) or (c and d):
        print("BoolOp Test")
