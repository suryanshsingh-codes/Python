# =============================================
# 4. TABLE OF A NUMBER
# =============================================
print("="*60)
print("4. TABLE OF A NUMBER")
print("="*60)
print()

n = int(input("Enter n : "))
print()

print(f"Value of n : {n}")
print()

for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")
print()