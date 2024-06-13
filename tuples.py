# Creating a tuple
my_tuple = (1, 2, 3, 'a', 'happy')

# Accessing elements
print(my_tuple[3])

# Attempting to change an element (will rase an error)
# my_tuple[0] = 10 TypeError: 'tuple' object does not support item assignment

# Tuples can be unpacked
a, b, c, d, e = my_tuple
print(a)

# Tuples can contain other tuples (nested tuples)
nested_tuple = (1, (2,3), (4,5), (0,0))
print(nested_tuple[1][1])