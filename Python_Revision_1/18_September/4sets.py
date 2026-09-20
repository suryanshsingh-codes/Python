# ===================================================================
# SET : THE UNORDERED UNIQUE DATA STRUCTURE
# ===================================================================
print("="*64)
print("SET")
print("="*64)
print()

# --------------------------------------------------
# BEFORE STARTING : 4 KEY TERMS
# --------------------------------------------------
print("----------SET POWERS / PROPERTIES----------")
print()

# --------------------------------------------------
# 1. MUTABLE : value CAN be changed after creation
# --------------------------------------------------
print("1. MUTABLE : Set values can be changed after creation")
mySet = {1, 2, 3}
print(f"mySet : {mySet}")
mySet.add(100)
print(f"After add(100) : {mySet}")
print()

# --------------------------------------------------
# 2. DUPLICATES : NOT allowed, every element is UNIQUE
# --------------------------------------------------
print("2. DUPLICATES : Not allowed, every element is unique")
mySet = {1, 2, 2, 3, 3, 3}
print(f"Set with duplicates removed : {mySet}")
print()

# --------------------------------------------------
# 3. UNORDERED : sequence is NOT maintained
# --------------------------------------------------
print("3. UNORDERED : Sequence is not maintained")
mySet = {10, 20, 30}
print(f"mySet : {mySet}")
# mySet[0]    # ❌ ERROR : set is not subscriptable
print()

# --------------------------------------------------
# 4. HETEROGENEOUS : only HASHABLE (immutable) types
# --------------------------------------------------
print("4. HETEROGENEOUS : only hashable (immutable) types allowed")
mySet = {"Surya", 21, 92.5, True, (1, 2)}
print(f"Mixed set : {mySet}")

# mySet = {[1, 2], 3}    # ❌ ERROR : list is not hashable
print()


# ================================================================
# HOW SET STORES VALUE IN PYTHON
# ================================================================
print("----------HOW SET STORES VALUE IN PYTHON----------")
print()

# --------------------------------------------------
# 1. Each value is hashed using hash( )
# --------------------------------------------------
print("1. Each value is hashed using hash( )")
print(f"hash(10)     = {hash(10)}")
print(f"hash('Surya') = {hash('Surya')}")
print()

# --------------------------------------------------
# 2. Hash is used as index to store element in memory
# --------------------------------------------------
print("2. Hash is used as index to store element in memory")
print("Since hashing does not maintain order, sets are unordered")
print()

# --------------------------------------------------
# 3. Only immutable ( hashable ) objects can be stored
# --------------------------------------------------
print("3. Only immutable ( hashable ) objects can be stored")
print("Allowed   : numbers, strings, tuples")
print("Not allowed : lists, dictionaries")
print()


# ================================================================
# SET BASICS
# ================================================================
print("----------SET BASICS----------")
print()

# --------------------------------------------------
# CREATING A SET : use curly braces { }
# --------------------------------------------------
print("1. CREATING A SET")
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
mixed = {"Surya", 21, 92.5, True}

print(f"fruits  = {fruits}")
print(f"numbers = {numbers}")
print(f"mixed   = {mixed}")
print()

# --------------------------------------------------
# SPECIAL CASE : empty set needs set( )
# --------------------------------------------------
print("2. EMPTY SET : use set( ) , not { }")
emptySet = set()      # ✅ empty set
notSet = {}           # ❌ this is an empty dict

print(f"emptySet = {emptySet} | type = {type(emptySet)}")
print(f"notSet   = {notSet}    | type = {type(notSet)}")
print()

# --------------------------------------------------
# INDEXING : NOT possible
# --------------------------------------------------
print("3. INDEXING : NOT possible")
print("Sets are unordered, so no index access")
print()


# ================================================================
# SET TRAVERSING
# ================================================================
print("----------SET TRAVERSING----------")
print()

# --------------------------------------------------
# Traversing : directly on elements ( no index )
# --------------------------------------------------
print("1. TRAVERSING : DIRECTLY ON ELEMENTS")
fruits = {"apple", "banana", "cherry"}
for fruit in fruits:
    print(f"Element = {fruit}")
print()


# ===================================================================
# SET METHODS
# ===================================================================
print("----------SET METHODS----------")
print()

# --------------------------------------------------
# 1. add( ) : add element
# --------------------------------------------------
print("1. add( )")
fruits = {"apple", "banana"}
print(f"Before add : {fruits}")
fruits.add("cherry")
print(f"After add  : {fruits}")
print()

# --------------------------------------------------
# 2. remove( ) : remove element ( error if not found )
# --------------------------------------------------
print("2. remove( )")
fruits = {"apple", "banana", "cherry"}
print(f"Before remove : {fruits}")
fruits.remove("banana")
print(f"After remove  : {fruits}")
print()

# --------------------------------------------------
# 3. discard( ) : remove element ( no error if not found )
# --------------------------------------------------
print("3. discard( )")
fruits = {"apple", "banana", "cherry"}
print(f"Before discard : {fruits}")
fruits.discard("banana")
fruits.discard("mango")     # no error
print(f"After discard  : {fruits}")
print()

# --------------------------------------------------
# 4. pop( ) : remove random element
# --------------------------------------------------
print("4. pop( )")
fruits = {"apple", "banana", "cherry"}
print(f"Before pop : {fruits}")
fruits.pop()
print(f"After pop  : {fruits}")
print()

# --------------------------------------------------
# 5. clear( ) : remove ALL elements
# --------------------------------------------------
print("5. clear( )")
fruits = {"apple", "banana", "cherry"}
print(f"Before clear : {fruits}")
fruits.clear()
print(f"After clear  : {fruits}")
print()

# --------------------------------------------------
# 6. len( ) : total number of elements
# --------------------------------------------------
print("6. len( )")
fruits = {"apple", "banana", "cherry"}
print(f"fruits : {fruits}")
print(f"Length : {len(fruits)}")
print()


# ===================================================================
# SET OPERATIONS BETWEEN 2 SETS
# ===================================================================
print("----------SET OPERATIONS BETWEEN 2 SETS----------")
print()

setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

print(f"setA : {setA}")
print(f"setB : {setB}")
print()

# --------------------------------------------------
# 1. UNION : all elements from both sets
# --------------------------------------------------
print("1. UNION : all elements from both sets")
print(f"setA.union(setB)  : {setA.union(setB)}")
print(f"setA | setB       : {setA | setB}")
print()

# --------------------------------------------------
# 2. INTERSECTION : common elements
# --------------------------------------------------
print("2. INTERSECTION : common elements")
print(f"setA.intersection(setB)  : {setA.intersection(setB)}")
print(f"setA & setB              : {setA & setB}")
print()

# --------------------------------------------------
# 3. DIFFERENCE : elements in A but not in B
# --------------------------------------------------
print("3. DIFFERENCE : elements in A but not in B")
print(f"setA.difference(setB)  : {setA.difference(setB)}")
print(f"setA - setB            : {setA - setB}")
print()

# --------------------------------------------------
# 4. SYMMETRIC DIFFERENCE : elements in either but not both
# --------------------------------------------------
print("4. SYMMETRIC DIFFERENCE : elements in either but not both")
print(f"setA.symmetric_difference(setB)  : {setA.symmetric_difference(setB)}")
print(f"setA ^ setB                      : {setA ^ setB}")
print()

# --------------------------------------------------
# 5. SUBSET : is A a subset of B ?
# --------------------------------------------------
print("5. SUBSET : is A a subset of B ?")
setA = {1, 2}
setB = {1, 2, 3, 4, 5}
print(f"setA : {setA}")
print(f"setB : {setB}")
print(f"setA.issubset(setB)  : {setA.issubset(setB)}")
print()

# --------------------------------------------------
# 6. SUPERSET : is A a superset of B ?
# --------------------------------------------------
print("6. SUPERSET : is A a superset of B ?")
setA = {1, 2, 3, 4, 5}
setB = {1, 2}
print(f"setA : {setA}")
print(f"setB : {setB}")
print(f"setA.issuperset(setB)  : {setA.issuperset(setB)}")
print()

# --------------------------------------------------
# 7. DISJOINT : no common elements ?
# --------------------------------------------------
print("7. DISJOINT : no common elements ?")
setA = {1, 2, 3}
setB = {4, 5, 6}
print(f"setA : {setA}")
print(f"setB : {setB}")
print(f"setA.isdisjoint(setB)  : {setA.isdisjoint(setB)}")
print()