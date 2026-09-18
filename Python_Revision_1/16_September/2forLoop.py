# =============================================
# FOR LOOPS
# =============================================
print("="*60)
print("FOR LOOPS")
print("="*60)
print()


print(f"Print 5 times with FOR loop: range(1,6)")
for i in range(1,6):
    print(f"Hello {i}th time.")
print()

print(f"Print 5 times with FOR loop: range(1,6,1)")
for i in range(1,6,1):
    print(f"Hello {i}th time.")
print()

print(f"Print 5 times with FOR loop: range(1,6,2)")
for i in range(1,6,2):
    print(f"Hello {i}th time.")
print()

print(f"Print 5 times with FOR loop: range(-5,-1)")
for i in range(-5,-1):
    print(f"Hello {i}th time.")
print()

print(f"Print 5 times with FOR loop: range(-5,-1,2)")
for i in range(-5,-1,2):
    print(f"Hello {i}th time.")
print()


# ---------------------------------------------------------
# EXTRA CASES — IMPORTANT FOR EXAMS
# ---------------------------------------------------------
print("-"*60)
print("EXTRA CASES")
print("-"*60)
print()

print(f"Only stop value : range(5)")
for i in range(5):
    print(f"Hello {i}th time.")
print()

print(f"Start and stop : range(2, 7)")
for i in range(2, 7):
    print(f"Hello {i}th time.")
print()

print(f"REVERSE loop : range(5, 0, -1)")
for i in range(5, 0, -1):
    print(f"Hello {i}th time.")
print()

print(f"REVERSE with step 2 : range(10, 0, -2)")
for i in range(10, 0, -2):
    print(f"Hello {i}th time.")
print()

print(f"Empty range : range(5, 1)")
for i in range(5, 1):
    print(f"Hello {i}th time.")
print("(kuch print nahi hoga kyunki range empty hai)")
print()