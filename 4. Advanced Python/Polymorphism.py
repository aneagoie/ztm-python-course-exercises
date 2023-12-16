# Polymorphism

# Parent Class
class User:
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('Do nothing.')


# Sub Class/ Child Class/ Derived Class
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with arrows: Arrows left- {self.num_arrows}')


wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robbin', 30)


def player_attack(char_):
    char_.attack()


player_attack(wizard1)
player_attack(archer1)

for char in [wizard1, archer1]:
    char.attack()
