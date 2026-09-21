# =============================================
# 2. SUM ALL VALUES IN A DICTIONARY
# =============================================
print("="*60)
print("2. SUM ALL VALUES IN A DICTIONARY")
print("="*60)
print()

marks = {"math": 80, "science": 90, "english": 70}
print(f"Value of marks : {marks}")
print()

total = 0
for index in marks:
    total += marks[index]
print(f"Sum : {total}")
print()