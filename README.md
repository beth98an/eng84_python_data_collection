# Data collections in Python

- Lists & tuples
- Dictionaries
- Sets

### What is a list 
- Lists are commonly used to store the data
- Lists are MUTABLE 
- Syntax [ ] used to create a list
```
shopping_list = ["bread", "chocolate", "avocados", "milk"]
print(shopping_list)
print(type(shopping_list))
```
- Indexing for Lists is the same as for strings
```
print(shopping_list[1])
print(shopping_list[-2])
```
#### Changing an item within a list
```
# change the value of 0 index from bread to orange
print(shopping_list)
shopping_list[0] = "orange"
print(shopping_list)
```
#### Adding and removing an item in a list

- Use the command `.append("item")` to add an item to a list.
```
shopping_list.append("ice cream")
print(shopping_list)
```
- Use `.remove("item")` to remove an item from a list.
```
shopping_list.remove("orange")
print(shopping_list)
```
- `.pop()` deletes the last item from the list.
```
shopping_list.pop()
print(shopping_list)
```
- You can mix data types in a list.
```
mixed_list = [1, 2, 3, "one", "two", "three"]
print(mixed_list)
```

### Tuples
- Tuples are exactly the same as Lists, but they are IMMUTABLE
- syntax ( ) for Tuples
```
essential = ("paracetamol", "toothpaste", "tea bags")
print(essential)
print(type(essential))

essential[0] = "cereal"  # will not work, Tuples are IMMUTABLE
```

### Dictionaries

- Dictionaries use KEY VALUE pairs to save data
- The data can be retrieved by using its value or key
- Syntax { }
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
print(dev_ops_student)
print(type(dev_ops_student))  # confirm the type
```
- Items in dictionaries can be retrieved using the methods below.
```
print(dev_ops_student["name"])
print(dev_ops_student["completed_lessons"])
print(dev_ops_student["completed_lessons_names"][1]) # for items within lists
```
- `.keys()` returns the keys in the dictionary
- `.values()` returns the values
```
print(dev_ops_student.keys())
print(dev_ops_student.values())
```
- Lists in dictionaries can be edited using the same methods as Lists
```
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
### Sets
- Sets are unordered
- syntax { }
```
car_parts = {"wheels", "windows", "doors"}
print(car_parts)
print(type(car_parts)) # confirms type
```
- `.add(item)` adds items to sets
- `.discard(item)` removes items from sets
```
car_parts.add("seats")
print(car_parts)
car_parts.discard("doors")
print(car_parts)
```