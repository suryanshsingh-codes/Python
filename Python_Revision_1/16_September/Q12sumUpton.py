# =============================================
# 5. SUM UPTO N TERMS
# =============================================
print("="*60)
print("5. SUM UPTO N TERMS")
print("="*60)
print()

n = int(input("Enter n : "))
print()

print(f"Value of n : {n}")
print()

total = 0
for i in range(1, n+1):
    total += i
print(f"Sum : {total}")
print()