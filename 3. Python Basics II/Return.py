# Return

def sum1(num1, num2):
    return num1 + num2


total = sum1(10, 5)
print(sum1(10, total))
print()


def sum2(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(num1, num2)


total = sum2(10, 20)
print(total)
