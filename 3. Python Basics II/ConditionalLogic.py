# Conditional Logic

is_old = True
is_licenced = True

if is_old:
    print('You are old enough to drive!')
elif is_licenced:
    print('You can drive now!')
else:
    print('You are not of age!')

print('ok ok')
print()

# improved version
if is_old and is_licenced:
    print('You are old enough to drive, and you have a licence!')
else:
    print('You are not of age!')

print('ok ok')
