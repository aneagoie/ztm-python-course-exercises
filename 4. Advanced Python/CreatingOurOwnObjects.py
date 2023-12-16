# Creating Our Own Objects

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('Run')


player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50

print(player1.name)
print(player2.name)
print(player1.age)
print(player2.age)
player1.run()
print(player2.attack)
