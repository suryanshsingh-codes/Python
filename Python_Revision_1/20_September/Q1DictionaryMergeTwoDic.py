# =============================================
# 1. MERGE TWO DICTIONARIES
# =============================================
print("="*60)
print("1. MERGE TWO DICTIONARIES")
print("="*60)
print()

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

print(f"Value of dict1 : {dict1}")
print(f"Value of dict2 : {dict2}")
print()

for index in dict2:
    dict1[index]=dict2[index]
print(f"Merged : {dict1}")
print()