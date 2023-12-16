# While loops

i = 0
while i < 50:
    print(i, end='\t')
    i += 1
else:
    print('\nDone with all the work.')
print()

my_list = [1, 2, 3]
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
print()

while True:
    response = input('Say Something: ')
    if response == 'bye':
        break
