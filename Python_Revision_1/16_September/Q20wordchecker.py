# =============================================
# 13. COUNT LETTERS, DIGITS, SYMBOLS
# =============================================
print("="*60)
print("13. COUNT LETTERS, DIGITS, SYMBOLS")
print("="*60)
print()

str1 = "P@#yn26at^&i5ve"
print(f"Value of str1 : {str1}")
print()

chars = 0
digits = 0
symbols = 0

for ch in str1:
    if ch.isalpha():
        chars += 1
    elif ch.isdigit():
        digits += 1
    else:
        symbols += 1

print("Total counts of chars, digits, and symbols")
print(f"Chars   = {chars}")
print(f"Digits  = {digits}")
print(f"Symbols = {symbols}")
print()