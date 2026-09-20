# ===================================================================
# 3. FIND THE GREATEST ELEMENT AND PRINT ITS INDEX
# ===================================================================
print("="*64)
print("FIND THE GREATEST ELEMENT AND PRINT ITS INDEX")
print("="*64)
print()

# --------------------------------------------------
# Sample list
# --------------------------------------------------
myList = [23, -45, 67, -12, 89, 34, -8, 90, 56, 11, 100]
print(f"myList : {myList}")
print()

# --------------------------------------------------
# Assume first element is the greatest
# --------------------------------------------------
greatest = myList[0]
greatestIndex = 0

# --------------------------------------------------
# Loop on each index and compare
# --------------------------------------------------
for i in range(len(myList)):
    if myList[i] > greatest:
        greatest = myList[i]
        greatestIndex = i

print(f"Greatest element : {greatest}")
print(f"Its index        : {greatestIndex}")
print()