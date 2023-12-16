# Exercise Find Duplicates
# Check for duplicates in the list.
# Print the characters which have duplicates in the list.

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

# for i in range(len(some_list)):
#     for j in range(i+1, len(some_list)):
#         if some_list[i] == some_list[j]:
#             duplicates.append(some_list[i])
#
# print(duplicates)
#
#
#
# duplicates = set()
#
# list_set = set(some_list)
#
# for char in list_set:
#     count = 0
#     for item in some_list:
#         if item == char:
#             count += 1
#     if count > 1:
#         duplicates.add(char)
#
# print(duplicates)
