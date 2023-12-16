# Docstrings

def test(a):
    """
    Info : This function tests and prints param a
    :param a:
    :return:
    """

    print(a)


test('!!!')

help(test)
print()
print(test.__doc__)
