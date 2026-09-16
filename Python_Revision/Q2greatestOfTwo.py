# =============================================
# Q1. GREATEST OF TWO NUMBERS
# =============================================
print("="*60)
print("Q1. GREATEST OF TWO NUMBERS")
print("="*60)
print()

a = int(input("Enter first number  : "))
b = int(input("Enter second number : "))

print(f"Value of a : {a}")
print(f"Value of b : {b}")

if a > b:
    print(f"{a} is the greatest")
elif b > a:
    print(f"{b} is the greatest")
else:
    print("Both numbers are equal")