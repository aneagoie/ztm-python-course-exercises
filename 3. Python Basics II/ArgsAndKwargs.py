# *args and **kwargs


def super_func(name, *args, i='hi', **kwargs):
    total = 0
    for item in kwargs.values():
        total += item
    print(i, name)
    return sum(args) + total


print(super_func('nitesh', 1, 2, 3, 4, 5, i='hello', num1=5, num2=10))

# Rule: params, *args, default parameters, **kwargs
