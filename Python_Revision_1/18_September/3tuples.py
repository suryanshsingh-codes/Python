# ===================================================================
# TUPLE : THE IMMUTABLE DATA STRUCTURE
# ===================================================================
print("="*64)
print("TUPLE")
print("="*64)
print()

# --------------------------------------------------
# BEFORE STARTING : 4 KEY TERMS
# --------------------------------------------------
print("----------TUPLE POWERS / PROPERTIES----------")
print()

# --------------------------------------------------
# 1. IMMUTABLE : value CANNOT be changed after creation
# --------------------------------------------------
print("1. IMMUTABLE : Tuple values cannot be changed after creation")
myTuple = (1, 2, 3)
print(f"myTuple : {myTuple}")
# myTuple[0] = 100    # ❌ ERROR : tuple is immutable
print()

# --------------------------------------------------
# 2. DUPLICATES : same value can occur MULTIPLE times
# --------------------------------------------------
print("2. DUPLICATES : Same value can occur multiple times")
myTuple = (1, 2, 2, 3, 3, 3)
print(f"Tuple with duplicates : {myTuple}")
print()

# --------------------------------------------------
# 3. ORDERED : sequence is MAINTAINED as inserted
# --------------------------------------------------
print("3. ORDERED : Sequence is maintained as inserted")
myTuple = (10, 20, 30)
print(f"myTuple : {myTuple}")
print(f"Index 0 = {myTuple[0]} | Index 1 = {myTuple[1]} | Index 2 = {myTuple[2]}")
print()

# --------------------------------------------------
# 4. HETEROGENEOUS : multiple data types in one tuple
# --------------------------------------------------
print("4. HETEROGENEOUS : Multiple data types in one tuple")
myTuple = ("Surya", 21, 92.5, True)
print(f"Mixed tuple : {myTuple}")
print()


# ================================================================
# TUPLE BASICS
# ================================================================
print("----------TUPLE BASICS----------")
print()

# --------------------------------------------------
# CREATING A TUPLE : use round brackets ( )
# --------------------------------------------------
print("1. CREATING A TUPLE")
fruits = ("apple", "banana", "cherry")
numbers = (1, 2, 3, 4, 5)
mixed = ("Surya", 21, 92.5, True)

print(f"fruits  = {fruits}")
print(f"numbers = {numbers}")
print(f"mixed   = {mixed}")
print()

# --------------------------------------------------
# SPECIAL CASE : single element tuple needs a COMMA
# --------------------------------------------------
print("2. SINGLE ELEMENT TUPLE : comma is mandatory")
singleTuple = (5,)      # ✅ tuple
notTuple = (5)          # ❌ this is just int 5

print(f"singleTuple = {singleTuple} | type = {type(singleTuple)}")
print(f"notTuple    = {notTuple}    | type = {type(notTuple)}")
print()

# --------------------------------------------------
# INDEXING : same as string / list
# --------------------------------------------------
print("3. INDEXING ( same as string / list )")
print(f"fruits[0]  = {fruits[0]}")
print(f"fruits[1]  = {fruits[1]}")
print(f"fruits[-1] = {fruits[-1]}")
print()

# --------------------------------------------------
# SLICING : same as string / list
# --------------------------------------------------
print("4. SLICING ( same as string / list )")
print(f"fruits[0:2]  = {fruits[0:2]}")
print(f"fruits[::-1] = {fruits[::-1]}")
print()

# --------------------------------------------------
# IMMUTABILITY
# --------------------------------------------------
print("5. IMMUTABILITY : STRING vs LIST vs TUPLE")

# tuple : CANNOT change
myTuple = ("P", "y", "t", "h", "o", "n")
print(f"myTuple : {myTuple}")
# myTuple[0] = "J"    # ❌ ERROR : tuple is immutable
print()


# ================================================================
# TUPLE TRAVERSING AND METHODS
# ================================================================
print("----------TUPLE TRAVERSING AND METHODS----------")
print()

# --------------------------------------------------
# TRAVERSING : using index values
# --------------------------------------------------
print("1. TRAVERSING : USING INDEX")
fruits = ("apple", "banana", "cherry")
for i in range(len(fruits)):
    print(f"Index {i} = {fruits[i]}")
print()

# --------------------------------------------------
# TRAVERSING : directly on elements
# --------------------------------------------------
print("2. TRAVERSING : DIRECTLY ON ELEMENTS")
for fruit in fruits:
    print(f"Element = {fruit}")
print()


# ===================================================================
# TUPLE METHODS : only 2 methods
# ===================================================================
print("----------TUPLE METHODS----------")
print()

# --------------------------------------------------
# 1. index( ) : find the INDEX of an element
# --------------------------------------------------
print("1. index( )")
fruits = ("apple", "banana", "cherry")
print(f"fruits : {fruits}")
print(f"Index of 'banana' : {fruits.index('banana')}")
print()

# --------------------------------------------------
# 2. count( ) : count how many times element appears
# --------------------------------------------------
print("2. count( )")
numbers = (1, 2, 2, 3, 3, 3)
print(f"numbers : {numbers}")
print(f"Count of 3 : {numbers.count(3)}")
print()

# ===================================================================
# TUPLE UNPACKING
# ===================================================================
print("="*64)
print("TUPLE UNPACKING")
print("="*64)
print()

# --------------------------------------------------
# Basic unpacking
# --------------------------------------------------
myTuple = (10, 20, 30)
a, b, c = myTuple

print(f"myTuple : {myTuple}")
print(f"a = {a} | b = {b} | c = {c}")
print()

# --------------------------------------------------
# Star unpacking
# --------------------------------------------------
myTuple = (10, 20, 30, 40, 50)
first, *middle, last = myTuple

print(f"myTuple : {myTuple}")
print(f"first  = {first}")
print(f"middle = {middle}")
print(f"last   = {last}")
print()

# --------------------------------------------------
# Swapping
# --------------------------------------------------
a = 10
b = 20
print(f"Before swap : a = {a} | b = {b}")

a, b = b, a
print(f"After swap  : a = {a} | b = {b}")
print()

print("="*64)