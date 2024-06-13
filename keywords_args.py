def greet(fname, lname):
    print(f"Hello, {fname} {lname}!!")

greet("Max", "Brenner")

# Using Keyword Arguments
greet(fname="Max", lname="Brenner")

greet(lname="Brenner", fname="Max")

def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

# Positional Arguments
describe_pet("Willie")

# Positional and default arguement
describe_pet("Harry", "Hamster")

# Keyword Arguments
describe_pet(animal_type="cat", pet_name="Whiskers")