# Get user's name as input
user_name = input("What is your name? ")

# Predefined name to compare with
my_name = "John"

# Check if the user's name matches my_name
if user_name.lower() == my_name.lower():
    print("Hey, we have the same name! We must be long-lost twins!")
else:
    print(f"Nice to meet you, {user_name}! But I think my name is better. 😉")
