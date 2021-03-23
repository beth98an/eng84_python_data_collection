# Dictionaries
# Dictionaries use KEY VALUE pairs to save data
# The data can be retrieved by its value or the key
# Syntax {}
# Within the dictionary we can also have lists declared

# Let's create one
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

# Sets ? The difference is that sets are unordered
# syntax {}

# Let's create a set
car_parts = {"wheels", "windows", "doors"}
print(car_parts)
print(type(car_parts))
car_parts.add("seats")
print(car_parts)
car_parts.discard("doors")
print(car_parts)
