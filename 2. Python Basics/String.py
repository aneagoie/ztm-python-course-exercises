# Strings

print(type('Hi Hello there!'))
username = 'SuperCoder'
password = "SuperSecret"
long_string = '''
WOW
o_o
___
'''
print(long_string)

first_name = 'Nitesh'
last_name = 'Kumar'
full_name = first_name + ' ' + last_name
print(full_name)
print("\n")

# String Concatenation

print('hello' + ' Nitesh')
print('hello ' + str(5))
print("\n")

# Type Conversion

print(type(int(str(100))))

a = str(100)
b = int(a)
c = type(b)
print(c)
print("\n")


# Escape Sequences

weather = "\t It\'s \"kind of\" sunny \n Hope you have a good day!"
print(weather)
print("\n")


# Formatted Strings

name = 'Nitesh'
age = 27
print('Hi' + name + '. You are' + str(age) + ' years olf.')
print(f'Hi {name}. You are {age} years old.')

# Python2 Formatted Strings
print('Hi {}. Your are {} years old.'.format(name, age))
print('Hi {1}. You are {0} years olf.'.format(age, name))
print('Hi {new_name}. You are {age} years old.'.format(new_name='Sally', age=100))
print('\n')


# String Indexes
# String Slicing
# [Start : Stop : Step-over]

selfish = '01234567'
#          01234567
print((selfish[0]))
print((selfish[7]))
print((selfish[0:2]))
print((selfish[0:7]))
print((selfish[0:8]))
print((selfish[0:8:2]))
print((selfish[1:5]))
print((selfish[::1]))
print((selfish[-1]))
print((selfish[-2]))
print((selfish[::-1]))
print((selfish[::-2]))
print('\n')


# Built-in Functions and Methods

print(len('Helllooooo'))
quote = 'to be or not to be'
print(quote.upper())
print(quote.capitalize())
print(quote.find('be'))
print(quote.replace('be', 'me'))
print(quote)
print('\n')
