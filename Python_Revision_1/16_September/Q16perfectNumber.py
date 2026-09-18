# =============================================
# 9. PERFECT NUMBER CHECK
# =============================================
print("="*60)
print("9. PERFECT NUMBER CHECK")
print("="*60)
print()

n = int(input("Enter n : "))
print()

print(f"Value of n : {n}")
print()

total = 0
for i in range(1, n):
    if n % i == 0:
        total += i

if total == n:
    print(f"{n} is a Perfect Number")
else:
    print(f"{n} is NOT a Perfect Number")
print()