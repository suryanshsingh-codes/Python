# ===================================================================
# 2. MEAN OF LIST ELEMENTS
# ===================================================================
print("="*64)
print("MEAN OF LIST ELEMENTS")
print("="*64)
print()

# --------------------------------------------------
# Sample list
# --------------------------------------------------
myList = [23, -45, 67, -12, 89, 34, -8, 90, 56, 11]
print(f"myList : {myList}")
print()

# --------------------------------------------------
# Calculate total using loop
# --------------------------------------------------
total = 0

for element in myList:
    total = total + element

# --------------------------------------------------
# Mean = total / number of elements
# --------------------------------------------------
mean = total / len(myList)

print(f"Total  : {total}")
print(f"Length : {len(myList)}")
print(f"Mean   : {mean}")
print()