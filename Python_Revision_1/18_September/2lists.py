# ===================================================================
# LIST : THE MOST USED DATA STRUCTURE
# ===================================================================
print("="*64)
print("LIST")
print("="*64)
print()

# --------------------------------------------------
# BEFORE STARTING : 4 KEY TERMS
# --------------------------------------------------
print("----------LIST POWERS / PROPERTIES----------")
print()

# --------------------------------------------------
# 1. MUTABLE : value can be CHANGED after creation
# --------------------------------------------------
print("1. MUTABLE : List values can be changed after creation")
myList = [1, 2, 3]
print(f"myList : {myList}")
myList[0] = 100
print(f"After changing index 0 : {myList}")
print()

# --------------------------------------------------
# 2. DUPLICATES : same value can occur MULTIPLE times
# --------------------------------------------------
print("2. DUPLICATES : Same value can occur multiple times")
myList = [1, 2, 2, 3, 3, 3]
print(f"List with duplicates : {myList}")
print()

# --------------------------------------------------
# 3. ORDERED : sequence is MAINTAINED as inserted
# --------------------------------------------------
print("3. ORDERED : Sequence is maintained as inserted")
myList = [10, 20, 30]
print(f"myList : {myList}")
print(f"Index 0 = {myList[0]} | Index 1 = {myList[1]} | Index 2 = {myList[2]}")
print()

# --------------------------------------------------
# 4. HETEROGENEOUS : multiple data types in one list
# --------------------------------------------------
print("4. HETEROGENEOUS : Multiple data types in one list")
myList = ["Surya", 21, 92.5, True]
print(f"Mixed list : {myList}")
print()


# ================================================================
# LIST BASICS
# ================================================================
print("----------LIST BASICS----------")
print()

# --------------------------------------------------
# CREATING A LIST : use square brackets [ ]
# --------------------------------------------------
print("1. CREATING A LIST")
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["Surya", 21, 92.5, True]

print(f"fruits  = {fruits}")
print(f"numbers = {numbers}")
print(f"mixed   = {mixed}")
print()

# --------------------------------------------------
# INDEXING : same as string
# --------------------------------------------------
print("2. INDEXING ( same as string )")
print(f"fruits[0]  = {fruits[0]}")
print(f"fruits[1]  = {fruits[1]}")
print(f"fruits[-1] = {fruits[-1]}")
print()

# --------------------------------------------------
# SLICING : same as string
# --------------------------------------------------
print("3. SLICING ( same as string )")
print(f"fruits[0:2]  = {fruits[0:2]}")
print(f"fruits[::-1] = {fruits[::-1]}")
print()

# --------------------------------------------------
# MUTABILITY : string vs list
# --------------------------------------------------
print("4. MUTABILITY : STRING vs LIST")

# string : CANNOT change
myString = "Python"
# myString[0] = "J"    # ❌ ERROR : string is immutable

# list : CAN change
myList = ["P", "y", "t", "h", "o", "n"]
print(f"myList : {myList}")
myList[0] = "J"
print(f"After changing list[0] : {myList}")
print()


# ================================================================
# LIST TRAVERSING AND METHODS
# ================================================================
print("----------LIST TRAVERSING AND METHODS----------")
print()

# --------------------------------------------------
# TRAVERSING : using index values
# --------------------------------------------------
print("1. TRAVERSING : USING INDEX")
fruits = ["apple", "banana", "cherry"]
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
# LIST METHODS
# ===================================================================
print("----------LIST METHODS----------")
print()

# --------------------------------------------------
# 1. append( ) : add element at the END
# --------------------------------------------------
print("1. append( )")
fruits = ["apple", "banana"]
print(f"Before append : {fruits}")
fruits.append("cherry")
print(f"After append  : {fruits}")
print()

# --------------------------------------------------
# 2. insert( ) : add element at a SPECIFIC index
# --------------------------------------------------
print("2. insert( )")
fruits = ["apple", "cherry"]
print(f"Before insert : {fruits}")
fruits.insert(1, "banana")
print(f"After insert(1, 'banana') : {fruits}")
print()

# --------------------------------------------------
# 3. remove( ) : remove element by VALUE
# --------------------------------------------------
print("3. remove( )")
fruits = ["apple", "banana", "cherry"]
print(f"Before remove : {fruits}")
fruits.remove("banana")
print(f"After remove('banana') : {fruits}")
print()

# --------------------------------------------------
# 4. pop( ) : remove element by INDEX ( default = last )
# --------------------------------------------------
print("4. pop( )")
fruits = ["apple", "banana", "cherry"]
print(f"Before pop() : {fruits}")
fruits.pop()
print(f"After pop()  : {fruits}")

fruits = ["apple", "banana", "cherry"]
print(f"Before pop(0) : {fruits}")
fruits.pop(0)
print(f"After pop(0)  : {fruits}")
print()

# --------------------------------------------------
# 5. sort( ) : sort elements in ASCENDING order
# --------------------------------------------------
print("5. sort( )")
numbers = [3, 1, 4, 1, 5, 9, 2]
print(f"Before sort : {numbers}")
numbers.sort()
print(f"After sort  : {numbers}")
print()

# --------------------------------------------------
# 6. reverse( ) : reverse the list
# --------------------------------------------------
print("6. reverse( )")
numbers = [1, 2, 3, 4, 5]
print(f"Before reverse : {numbers}")
numbers.reverse()
print(f"After reverse  : {numbers}")
print()

# --------------------------------------------------
# 7. index( ) : find the INDEX of an element
# --------------------------------------------------
print("7. index( )")
fruits = ["apple", "banana", "cherry"]
print(f"fruits : {fruits}")
print(f"Index of 'banana' : {fruits.index('banana')}")
print()

# --------------------------------------------------
# 8. count( ) : count how many times element appears
# --------------------------------------------------
print("8. count( )")
numbers = [1, 2, 2, 3, 3, 3]
print(f"numbers : {numbers}")
print(f"Count of 3 : {numbers.count(3)}")
print()

# --------------------------------------------------
# 9. len( ) : total number of elements
# --------------------------------------------------
print("9. len( )")
fruits = ["apple", "banana", "cherry"]
print(f"fruits : {fruits}")
print(f"Length : {len(fruits)}")
print()

# --------------------------------------------------
# 10. clear( ) : remove ALL elements
# --------------------------------------------------
print("10. clear( )")
fruits = ["apple", "banana", "cherry"]
print(f"Before clear : {fruits}")
fruits.clear()
print(f"After clear  : {fruits}")
print()