# =============================================
# WHILE LOOP
# =============================================
print("="*60)
print("WHILE LOOP")
print("="*60)
print()


# 1. BASIC WHILE LOOP
print("1. BASIC WHILE LOOP")
print()

i = 1
while i <= 5:
    print(f"i : {i}")
    i += 1
print()


# 2. REVERSE WHILE LOOP
print("2. REVERSE WHILE LOOP")
print()

i = 5
while i >= 1:
    print(f"i : {i}")
    i -= 1
print()


# 3. WHILE LOOP WITH USER INPUT
print("3. WHILE LOOP WITH USER INPUT")
print()

n = int(input("Enter n : "))
print()

print(f"Value of n : {n}")
print()

i = 1
while i <= n:
    print(i)
    i += 1
print()
