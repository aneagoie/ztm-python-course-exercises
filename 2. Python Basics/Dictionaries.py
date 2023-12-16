# Dictionaries

dictionary = {
    'a': [1, 2, 3],
    'b': 'Hello',
    'c': True
}

print(dictionary['a'][1])
print(dictionary)
print('\n')


# Dictionary Methods

user = {
    'basket': [1, 2, 3],
    'greet': 'Hello',
    'age': 20
}

print(user.get('age', 55))

user2 = dict(name='JohnJohn')
print(user2)

print('basket' in user)
print('size' in user)
print('age' in user.keys())
print('Hello' in user.values())
print(user.items())

user2 = user.copy()
user.clear()
print(user)
print(user2)
print(user2.pop('age'))
print(user2.popitem())
user2.update({'age': 55})
print(user2)
print('\n')
