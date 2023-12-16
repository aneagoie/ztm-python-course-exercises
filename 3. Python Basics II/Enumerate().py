# Enumerate()

for i, char in enumerate('Helllooo'):
    print(i, char)

for i, char in enumerate([1, 2, 3]):
    print(i, char)

for i, char in enumerate(range(100)):
    if char == 50:
        print(f"index of 50 is: {i}")
