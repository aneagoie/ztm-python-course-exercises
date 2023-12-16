# Exercise Functions
# Highest Even: Write a function to find the highest even number from the list.


def highest_even(li):
    evens = []
    for item in li:
        if not item % 2 and item not in evens:
            evens.append(item)
    return max(evens)


print(highest_even([10, 2, 3, 4, 8, 11]))
