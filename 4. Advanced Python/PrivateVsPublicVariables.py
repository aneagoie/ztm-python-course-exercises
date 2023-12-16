# Private Vs Public Variables

class PlayerCharacter:
    def __init__(self, name, age):
        if age > 18:
            self._name = name
            self._age = age

    def speak(self):
        print(f'My name is {self._name} and I am {self._age} years old.')


player1 = PlayerCharacter('Tom', 20)
player1.speak()
