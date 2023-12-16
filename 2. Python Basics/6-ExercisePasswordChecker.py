# Exercise Password Checker

username = input('Enter your username:\t')
password = input('Enter you password:\t')

secret_password = len(password) * '*'
print(f'Hey {username}, your password {secret_password} is {len(password)}  letters long.')
