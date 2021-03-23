# Data collections in Python

- Lists & tuples
- Dict

### What is a list 
- Lists are commonly used to store the data
- Lists are MUTABLE 
- Syntax [] used to create a list

```python
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
```

### Tuples
- The difference between Lists and Tuples?
- syntax () for Tuples
- Tuples are exactly the same as Lists, but they are IMMUTABLE
```
essential = ("paracetamol", "toothpaste", "tea bags")
print(essential)
print(type(essential))

# essential[0] = "cereal"  # will not work
```
### Dictionaries
- Dictionaries use KEY VALUE pairs to save data
- The data can be retrieved by its value or the key
- Syntax {}
- Within the dictionary we can also have lists declared
```
dev_ops_student = {
    # "key": "value",
    "name": "James",
    "stream": "devops",
    "completed_lessons": 3,
    "completed_lessons_names": ["variables", "data types", "collections"]
    # key               value:      0           1                  2
}
# print(dev_ops_student)
# print(type(dev_ops_student))  # confirm the type
#
# print(dev_ops_student["name"])
# print(dev_ops_student["completed_lessons"])
# print(dev_ops_student["completed_lessons_names"][1])
#
# print(dev_ops_student.keys())
# print(dev_ops_student.values())

# add "operators" in completed lesson
dev_ops_student["completed_lessons_names"].append("operators")
print(dev_ops_student)

# change the completed lesson from 3 to 4
dev_ops_student["completed_lessons"] = 4
print(dev_ops_student)

# remove the "data type" from completed_lesson_names
dev_ops_student["completed_lessons_names"].remove("data types")
print(dev_ops_student)
```
