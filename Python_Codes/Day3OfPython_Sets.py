print("\n-------->Starting My Python Journey Now : DAY 3 : Sets, Set Traversing, Set Methods<--------\n")
# 3. SETS
    #Set Traversing
mySet1={1,2,3}
print(mySet1, " is my Set")
for i in mySet1:
    print(f" {i} is the element of my Set and {hash(i)} is its hash value")
print("\n")

    #Set methods
mySet1.add(4)
print(mySet1, ": 4 is added to my Set")

mySet1.remove(4)
print(mySet1, ": 4 is now removed from my Set")

mySet1.discard(32)
print(mySet1, ": 32 was discarded")

popElementOfSet=mySet1.pop()
print(popElementOfSet, " is the popped element")
print(mySet1, "is now updated Set")

mySet1.clear()
print(mySet1, " The Set was set to Clear")
print("\n")
    # 2. SET OPERATIONS
mySet1={1,2,3}
mySet2={3,4,5}
print(f"mySet1= {mySet2} and \nmySet2= {mySet2}\n")
print("Union of the two set")
union=mySet1.union(mySet2)
print(union)

print("Intersection of the two set")
intersection=mySet1.intersection(mySet2)
print(intersection)

print("Difference of the two set")
difference=mySet1.difference(mySet2)
print(difference)

print("Symmetric Difference of the two set")
symmetricDifference=mySet1.symmetric_difference(mySet2)
print(symmetricDifference)
