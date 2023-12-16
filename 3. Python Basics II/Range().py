# Range()

print(range(100))
print(range(0, 100))

for number in range(10):
    print(number, end=' ')
print()

for _ in range(10):
    print('Hi', end=' ')
print()

for number in range(0, 10, 2):
    print(number, end=' ')
print()

for number in range(0, 10, -1):
    print(number, end=' ')
print()

for number in range(10, 0, -1):
    print(number, end=' ')
print()

for number in range(10, 0):
    print(number, end=' ')
print()

for number in range(10, 0, -2):
    print(number, end=' ')
print()

for _ in range(2):
    print(list(range(10)))
