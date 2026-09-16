# =============================================
# OPERATORS
# =============================================
print("="*60)
print("OPERATORS")
print("="*60)
print()

# --------------------------------------------------------- 
# 4. LOGICAL OPERATORS : VALUES ALWAYS IN TRUE OR FALSE
# --------------------------------------------------------- 
print("-"*60)
print("4. LOGICAL OPERATORS")
print("-"*60)
print()

x = True
print(f"Value of x : {x}")
y = False
print(f"Value of y : {y}")
print()

print(f"1. Logical AND : x and y")
print(f"{x and y}")
print()

print(f"2. Logical AND : x and x")
print(f"{x and x}")
print()

print(f"3. Logical AND : y and y")
print(f"{y and y}")
print()

print(f"4. Logical OR : x or y")
print(f"{x or y}")
print()

print(f"5. Logical OR : x or x")
print(f"{x or x}")
print()

print(f"6. Logical OR : y or y")
print(f"{y or y}")
print()

print(f"7. Logical NOT : not x")
print(f"{not x}")
print()

print(f"8. Logical NOT : not y")
print(f"{not y}")
print()

# --------------------------------------------------------- 
# COMBINED / CHAINED LOGICAL OPERATORS
# --------------------------------------------------------- 
print("-"*60)
print("COMBINED LOGICAL OPERATORS")
print("-"*60)
print()

a = 23
print(f"Value of a : {a}")
b = 43
print(f"Value of b : {b}")
print()

print(f"9. a > 10 and b > 10")
print(f"{a > 10 and b > 10}")
print()

print(f"10. a > 30 and b > 30")
print(f"{a > 30 and b > 30}")
print()

print(f"11. a > 30 or b > 30")
print(f"{a > 30 or b > 30}")
print()

print(f"12. a > 30 or b < 30")
print(f"{a > 30 or b < 30}")
print()

print(f"13. not (a > 10)")
print(f"{not (a > 10)}")
print()

print(f"14. (a > 10) and (b > 10) or (a < 5)")
print(f"{(a > 10) and (b > 10) or (a < 5)}")
print()