# Lists

li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c']
li3 = [1, 2.5, 'a', True]
amazon_cart = ['notebooks', 'sunglasses']
print(amazon_cart[0])
print('\n')


# List Slicing
# [Start : Stop : Step-Over]

amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']
print(amazon_cart)
print(amazon_cart[0:2])
print(amazon_cart[0::2])
print(amazon_cart[::-1])

amazon_cart[0] = 'laptop'
print(amazon_cart)

new_cart = amazon_cart[:]
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

new_cart1 = amazon_cart
new_cart1[0] = 'gum'
print(new_cart1)
print(amazon_cart)
print('\n')


# Matrix

matrix = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]
print(matrix)
print(matrix[0][2])
print('\n')


# List Methods

basket = [1, 2, 3, 4, 5]

# Adding
new_list = basket.append(100)
print(basket)
print(new_list)
basket.insert(4, 50)
print(basket)
basket.extend([10, 20, 30, 40])
print(basket)
print('\n')

# Removing
basket.pop()
print(basket)
basket.pop(4)
print(basket)
basket.remove(100)
print(basket)
# basket.clear()
# print(basket)
print('\n')

print(basket.index(5))
print(5 in basket)
print(basket.count(4))
print('\n')

basket.sort()
print(basket)
new_basket = basket.copy()
new_basket.sort(reverse=True)
print(new_basket)
print(sorted(new_basket))
basket.reverse()
print(basket)
print('\n')


# Common List Patterns

print(basket[::-1])
print(range(1, 100))
print(list(range(101)))

sentence = '! '
new_sentence = sentence.join(['Hi', 'my', 'name', 'is', 'JOJO'])
print(new_sentence)
print('\n')


# List Unpacking

a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(other)
print(d)
