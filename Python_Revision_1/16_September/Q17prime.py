# =============================================
# 10. PRIME NUMBER CHECK
# =============================================
print("="*60)
print("10. PRIME NUMBER CHECK")
print("="*60)
print()

n = int(input("Enter n : "))
print()

print(f"Value of n : {n}")
print()

count = 0
for i in range(1, n+1):
    if n % i == 0:
        count += 1

if count == 2:
    print(f"{n} is a Prime Number")
else:
    print(f"{n} is NOT a Prime Number")
print()