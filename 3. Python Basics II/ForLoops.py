# For Loops

for item in 'Zero to Mastery':
    print(item, end=' ')
print()

for item in [1, 2, 3, 4, 5]:
    print(item, end=' ')
print()

for item in {1, 2, 3, 4, 5}:
    print(item, end=' ')
print()

for item in (1, 2, 3, 4, 5):
    print(item, end=' ')
print(item)
print()

# Nested Loops
for item in (1, 2, 3, 4, 5):
    for x in ['a', 'b', 'c']:
        print(item, x, end='\t')
