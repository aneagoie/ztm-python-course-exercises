# Attributes And Methods

class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name, age):
        if self.membership:     # Or PLayerCharacter.membership
            self.name = name
            self.age = age

    def shout(self):
        print(f'My name is {self.name}')

    def run(self, hello):
        print(f'{hello} {self.name}')


player1 = PlayerCharacter('Cindy', 44)
player1.shout()
player1.run('Hi')
print(player1.membership, '\t', player1.name, '\t', player1.age)
