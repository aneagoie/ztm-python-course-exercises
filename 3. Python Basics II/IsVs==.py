# Is vs ==

print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])
print()

print(True == True)
print('1' == 1)
print([1, 2, 3] == [1, 2, 3])
print()

print(True is 1)
print('1' is 1)
print([] is 1)
print(10 is 10.0)
print([1, 2, 3] is [1, 2, 3])
print()

print(True is True)
print('1' is '1')
print([] is [])
