# =============================================
# 6. FACTORIAL OF A NUMBER
# =============================================
print("="*60)
print("6. FACTORIAL OF A NUMBER")
print("="*60)
print()

n = int(input("Enter n : "))
print()

print(f"Value of n : {n}")
print()

fact = 1
for i in range(1, n+1):
    fact *= i
print(f"Factorial : {fact}")
print()