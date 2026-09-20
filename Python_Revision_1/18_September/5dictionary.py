# ===================================================================
# DICTIONARY : THE KEY - VALUE DATA STRUCTURE
# ===================================================================
print("="*64)
print("DICTIONARY")
print("="*64)
print()

# --------------------------------------------------
# BEFORE STARTING : 4 KEY TERMS
# --------------------------------------------------
print("----------DICTIONARY POWERS / PROPERTIES----------")
print()

# --------------------------------------------------
# 1. MUTABLE : can change, add or remove key-value pairs
# --------------------------------------------------
print("1. MUTABLE : can change, add or remove key-value pairs")
myDict = {"name": "Surya", "age": 21}
print(f"myDict : {myDict}")

myDict["age"] = 22
print(f"After changing age : {myDict}")

myDict["city"] = "Mumbai"
print(f"After adding city  : {myDict}")
print()

# --------------------------------------------------
# 2. KEYS are UNIQUE : values can have duplicates
# --------------------------------------------------
print("2. KEYS are UNIQUE : values can have duplicates")
myDict = {"a": 1, "b": 2, "c": 2, "d": 1}
print(f"myDict : {myDict}")
print("Keys are unique, values can repeat")
print()

# --------------------------------------------------
# 3. ORDERED : follows insertion order
# --------------------------------------------------
print("3. ORDERED : follows insertion order")
myDict = {"first": 1, "second": 2, "third": 3}
print(f"myDict : {myDict}")
print("Order is maintained as inserted")
print()

# --------------------------------------------------
# 4. HETEROGENEOUS : different types of keys and values
# --------------------------------------------------
print("4. HETEROGENEOUS : different types of keys and values")
myDict = {
    "name": "Surya",
    21: "age",
    92.5: [1, 2, 3],
    True: {"nested": "dict"}
}
print(f"Mixed dict : {myDict}")
print()


# ================================================================
# DICTIONARY BASICS
# ================================================================
print("----------DICTIONARY BASICS----------")
print()

# --------------------------------------------------
# CREATING A DICTIONARY : use curly braces { key : value }
# --------------------------------------------------
print("1. CREATING A DICTIONARY")
student = {
    "name": "Surya",
    "age": 21,
    "marks": 92.5,
    "isPassed": True
}

print(f"student = {student}")
print()

# --------------------------------------------------
# ACCESSING VALUES : use key ( like index in list )
# --------------------------------------------------
print("2. ACCESSING VALUES using key")
print(f"student['name']    = {student['name']}")
print(f"student['age']     = {student['age']}")
print(f"student['marks']   = {student['marks']}")
print()

# --------------------------------------------------
# CRUD OPERATIONS on values
# --------------------------------------------------
print("3. CRUD OPERATIONS on values")

# CREATE
student["city"] = "Mumbai"
print(f"After CREATE city  : {student}")

# READ
print(f"READ name          : {student['name']}")

# UPDATE
student["age"] = 22
print(f"After UPDATE age   : {student['age']}")

# DELETE
del student["isPassed"]
print(f"After DELETE isPassed : {student}")
print()


# ================================================================
# DICTIONARY TRAVERSING
# ================================================================
print("----------DICTIONARY TRAVERSING----------")
print()

student = {
    "name": "Surya",
    "age": 21,
    "marks": 92.5
}
print(f"student : {student}")
print()

# --------------------------------------------------
# 1. Traversing : default loop on KEYS
# --------------------------------------------------
print("1. TRAVERSING : DEFAULT LOOP ON KEYS")
for key in student:
    print(f"Key = {key} | Value = {student[key]}")
print()

# --------------------------------------------------
# 2. Traversing : using keys( ) method
# --------------------------------------------------
print("2. TRAVERSING : USING keys( )")
for key in student.keys():
    print(f"Key = {key}")
print()

# --------------------------------------------------
# 3. Traversing : using values( ) method
# --------------------------------------------------
print("3. TRAVERSING : USING values( )")
for value in student.values():
    print(f"Value = {value}")
print()

# --------------------------------------------------
# 4. Traversing : using items( ) method : key + value
# --------------------------------------------------
print("4. TRAVERSING : USING items( ) : key + value")
for key, value in student.items():
    print(f"{key} = {value}")
print()


# ===================================================================
# DICTIONARY METHODS
# ===================================================================
print("----------DICTIONARY METHODS----------")
print()

# --------------------------------------------------
# 1. keys( ) : get all keys
# --------------------------------------------------
print("1. keys( )")
student = {"name": "Surya", "age": 21, "marks": 92.5}
print(f"student : {student}")
print(f"Keys    : {student.keys()}")
print()

# --------------------------------------------------
# 2. values( ) : get all values
# --------------------------------------------------
print("2. values( )")
print(f"student : {student}")
print(f"Values  : {student.values()}")
print()

# --------------------------------------------------
# 3. items( ) : get all key-value pairs
# --------------------------------------------------
print("3. items( )")
print(f"student : {student}")
print(f"Items   : {student.items()}")
print()

# --------------------------------------------------
# 4. get( ) : get value safely ( no error if key missing )
# --------------------------------------------------
print("4. get( )")
print(f"student : {student}")
print(f"get('name')    : {student.get('name')}")
print(f"get('city')    : {student.get('city')}")
print(f"get('city', 'NA') : {student.get('city', 'NA')}")
print()

# --------------------------------------------------
# 5. update( ) : add or update multiple key-value pairs
# --------------------------------------------------
print("5. update( )")
student = {"name": "Surya", "age": 21}
print(f"Before update : {student}")

student.update({"age": 22, "city": "Mumbai"})
print(f"After update  : {student}")
print()

# --------------------------------------------------
# 6. pop( ) : remove key and return its value
# --------------------------------------------------
print("6. pop( )")
student = {"name": "Surya", "age": 21, "marks": 92.5}
print(f"Before pop : {student}")

removed = student.pop("age")
print(f"Removed value : {removed}")
print(f"After pop  : {student}")
print()

# --------------------------------------------------
# 7. popitem( ) : remove and return last key-value pair
# --------------------------------------------------
print("7. popitem( )")
student = {"name": "Surya", "age": 21, "marks": 92.5}
print(f"Before popitem : {student}")

removed = student.popitem()
print(f"Removed item : {removed}")
print(f"After popitem : {student}")
print()

# --------------------------------------------------
# 8. clear( ) : remove ALL key-value pairs
# --------------------------------------------------
print("8. clear( )")
student = {"name": "Surya", "age": 21}
print(f"Before clear : {student}")

student.clear()
print(f"After clear  : {student}")
print()

# --------------------------------------------------
# 9. len( ) : total number of key-value pairs
# --------------------------------------------------
print("9. len( )")
student = {"name": "Surya", "age": 21, "marks": 92.5}
print(f"student : {student}")
print(f"Length  : {len(student)}")
print()

# --------------------------------------------------
# 10. in : check if key exists
# --------------------------------------------------
print("10. in : check if key exists")
student = {"name": "Surya", "age": 21}
print(f"student : {student}")
print(f"'name' in student : {'name' in student}")
print(f"'city' in student : {'city' in student}")
print()
