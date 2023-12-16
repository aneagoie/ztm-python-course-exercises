# Break, Continue, Pass

my_list = [1, 2, 3]
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    continue
print()

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    break
print()

i = 0
while i < len(my_list):
    i += 1
    pass

print("No error")
