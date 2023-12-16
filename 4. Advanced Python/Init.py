# __init__

class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name, age):
        if age > 18:
            self.name = name
            self.age = age

    def shout(self):
        print(f'My name is {self.name}')


player1 = PlayerCharacter('Tom', 20)
print(player1.shout())
