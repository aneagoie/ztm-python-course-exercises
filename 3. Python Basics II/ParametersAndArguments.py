# Parameters and Arguments

# Parameters // Positional Parameters
def say_hello(name, emoji):
    print(f'helllooooo {name} {emoji}')


# Arguments // Positional Arguments
say_hello('Nitesh', ':)')
say_hello('Emily', ':p')
say_hello('Dah', ':\'(')
print()


# Default Parameters
def say_hello(name='Darth Vader', emoji='>:('):
    print(f'helllooooo {name} {emoji}')


# Keyword Arguments
say_hello(emoji=':)', name='Bibi')
say_hello()
say_hello('Timmy')
