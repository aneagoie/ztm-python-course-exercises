# Scope Rules

a = 1


def parent():
    a = 10

    def confusion():
        a = 5
        return a
    return confusion()


print(a)
print(parent())
print(sum)
