# =============================================
# 4. COMBINE TWO DICTIONARIES (ADD COMMON KEYS)
# =============================================
print("="*60)
print("4. COMBINE TWO DICTIONARIES (ADD COMMON KEYS)")
print("="*60)
print()

dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 5, "c": 15, "d": 25}

print(f"Value of dict1 : {dict1}")
print(f"Value of dict2 : {dict2}")
print()

for index in dict2:
    if index in dict1:
        dict1[index] += dict2[index]
    else:
        dict1[index] = dict2[index]
print(f"Combined : {dict1}")
print()