# ===================================================================
# 4. FIND THE SECOND GREATEST ELEMENT
# ===================================================================
print("="*64)
print("FIND THE SECOND GREATEST ELEMENT")
print("="*64)
print()

# --------------------------------------------------
# Sample list
# --------------------------------------------------
myList = [23, -45, 67, -12, 87, 34, -8, 90, 56, 11, 89]
print(f"myList : {myList}")
print()

# --------------------------------------------------
# Assume first element is greatest and second greatest
# --------------------------------------------------
greatest = myList[0]
secondGreatest = myList[0]

# --------------------------------------------------
# Loop on each element and update both
# --------------------------------------------------
for element in myList:
    if element > greatest:
        secondGreatest = greatest
        greatest = element
    elif element > secondGreatest and element != greatest:
        secondGreatest = element

print(f"Greatest        : {greatest}")
print(f"Second Greatest : {secondGreatest}")
print()