# =============================================
# 12. PALINDROME CHECK
# =============================================
print("="*60)
print("12. PALINDROME CHECK")
print("="*60)
print()

s = input("Enter a string : ")
print()

print(f"Value of s : {s}")
print()

rev = ""
for ch in s:
    rev = ch + rev

if s == rev:
    print(f"'{s}' is a Palindrome")
else:
    print(f"'{s}' is NOT a Palindrome")
print()