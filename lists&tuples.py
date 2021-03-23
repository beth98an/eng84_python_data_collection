# What is a list
# Lists are commonly used to store the data
# Lists are MUTABLE
# Syntax [] used to create a list

shopping_list = ["bread", "chocolate", "avocados", "milk"]
print(shopping_list)
print(type(shopping_list))
print(shopping_list[1])
print(shopping_list[-2])
# change the value of 0 index from bread to orange
print(shopping_list)
shopping_list[0] = "orange"
print(shopping_list)

shopping_list.append("ice cream")
print(shopping_list)

shopping_list.remove("orange")
print(shopping_list)

# pop() deletes the last item from the list
shopping_list.pop()
print(shopping_list)

# Can we mix data types in a list? yes
mixed_list = [1, 2, 3, "one", "two", "three"]
print(mixed_list)

# Tuples - The difference between Lists and Tuples?
# syntax () for Tuples
# Tuples are exactly the same as Lists, but they are IMMUTABLE
essential = ("paracetamol", "toothpaste", "tea bags")
print(essential)
print(type(essential))

# essential[0] = "cereal"  # will not work
# print(essential)
