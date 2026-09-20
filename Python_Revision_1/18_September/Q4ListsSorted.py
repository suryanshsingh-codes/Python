# ===================================================================
# 5. CHECK IF LIST IS SORTED OR NOT
# ===================================================================
print("="*64)
print("CHECK IF LIST IS SORTED OR NOT")
print("="*64)
print()

# --------------------------------------------------
# Sample list
# --------------------------------------------------
myList = [23, -45, 67, -12, 89, 34, -8, 90, 56, 11]
print(f"myList : {myList}")
print()

# --------------------------------------------------
# Assume the list is sorted
# --------------------------------------------------
isSorted = True

# --------------------------------------------------
# Loop and compare each element with the next one
# --------------------------------------------------
for i in range(len(myList) - 1):
    if myList[i] > myList[i + 1]:
        isSorted = False
        break

# --------------------------------------------------
# Print the result
# --------------------------------------------------
if isSorted:
    print("List is SORTED")
else:
    print("List is NOT SORTED")

print()