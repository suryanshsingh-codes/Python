# =============================================
# BREAK, CONTINUE, ELSE
# =============================================
print("="*60)
print("BREAK, CONTINUE, ELSE")
print("="*60)
print()

n = 5
print(f"Value of n : {n}")
print()


for i in range(1, 11):
    if i == 5:
        print("Skip 5")
        continue
    elif i ==10:
        print("Exit 10")
        break
    else:
        print(f"{n} x {i} = {n*i}")
print()