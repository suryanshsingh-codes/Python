# ===================================================================
# 1. PRINT POSITIVE AND NEGATIVE ELEMENTS
# ===================================================================
print("="*64)
print("PRINT POSITIVE AND NEGATIVE ELEMENTS")
print("="*64)
print()

# --------------------------------------------------
# Sample list
# --------------------------------------------------
myList = [23, -45, 67, -12, 89, 34, -8, 90, 56, 11]
print(f"myList : {myList}")
print()

# --------------------------------------------------
# Loop on each element and separate positive / negative
# --------------------------------------------------
positiveList = []
negativeList = []

for element in myList:
    if element > 0:
        positiveList.append(element)
    elif element < 0:
        negativeList.append(element)

print(f"Positive elements : {positiveList}")
print(f"Negative elements : {negativeList}")
print()