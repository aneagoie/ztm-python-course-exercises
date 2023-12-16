# Exercise Logical Operators

is_magician = False
is_expert = True

# Check if magician and expert: "you are a master magician"
if is_magician and is_expert:
    print("You are a master magician")

# Check if magician but not expert: "at least you're getting there"
if is_magician and not is_expert:
    print("At least you\'re getting there.")

# Check if not a magician: "You need magic powers"
if not is_magician:
    print("You need magic powers.")
