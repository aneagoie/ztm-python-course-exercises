# Dunder Methods

class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict= {
            'name': 'Yoyo',
            'has_pets': False
        }

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    # def __del__(self):
    #     print('deleted!')

    def __call__(self):
        return 'Yess?'

    def __getitem__(self, i):
        return self.my_dict[i]

    def __abs__(self, num):
        return num

    def __hex__(self):
        return 6

    def __set__(self):
        return 'done setting'


action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
# del action_figure
print(action_figure())
print(action_figure['name'])
print(action_figure.__abs__(-50))
print(action_figure.__hex__())
print(action_figure.__set__())
