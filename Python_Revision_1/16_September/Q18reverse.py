# =============================================
# 11. REVERSE A STRING
# =============================================
print("="*60)
print("11. REVERSE A STRING")
print("="*60)
print()

s = input("Enter a string : ")
print()

print(f"Value of s : {s}")
print()

rev = ""
for ch in s:
    rev = ch + rev

print(f"Original : {s}")
print(f"Reversed : {rev}")
print()