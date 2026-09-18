# =============================================
# 8. FACTORS OF A NUMBER
# =============================================
print("="*60)
print("8. FACTORS OF A NUMBER")
print("="*60)
print()

n = int(input("Enter n : "))
print()

print(f"Value of n : {n}")
print()

print(f"Factors of {n} : ", end="")
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")
print()
print()