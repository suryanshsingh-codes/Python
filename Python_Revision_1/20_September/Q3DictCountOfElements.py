# =============================================
# 3. COUNT FREQUENCY OF EACH ELEMENT
# =============================================
print("="*60)
print("3. COUNT FREQUENCY OF EACH ELEMENT")
print("="*60)
print()

name = "suryaaa"
print(f"Value of name : {name}")
print()

frequency = {}
for ch in name:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1
print(f"Frequency : {frequency}")
print()