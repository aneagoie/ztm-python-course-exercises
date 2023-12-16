# @classmethod and @staticmethod

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player3 = PlayerCharacter.adding_things(2, 3)   # Instantiated class using classmethod
print(player3)
print(PlayerCharacter.adding_things2(5, 9))
