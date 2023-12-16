# Functions

def say_hello():
    print('Helllooooo!')


say_hello()
print()

picture = [
  [0, 0, 0, 1, 0, 0, 0],
  [0, 0, 1, 1, 1, 0, 0],
  [0, 1, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 1],
  [0, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0]
]


def show_tree():
    for array in picture:
        for item in array:
            if item:
                print('*', end='')
            else:
                print(' ', end='')
        print()


show_tree()
print()
show_tree()
print()
show_tree()
print()
