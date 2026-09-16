# =============================================
# CONDITIONAL STATEMENTS
# =============================================
print("="*60)
print("CONDITIONAL STATEMENTS")
print("="*60)
print()

# ---------------------------------------------------------
# 1. SIMPLE IF
# ---------------------------------------------------------
print("-"*60)
print("1. SIMPLE IF")
print("-"*60)
print()

a = 23
print(f"Value of a : {a}")

if a > 10:
    print(f"a is greater than 10")

if a > 30:
    print(f"a is greater than 30")
print("(this line always prints because it is outside the if)")
# ---------------------------------------------------------
# 2. IF - ELSE
# ---------------------------------------------------------
print("-"*60)
print("2. IF - ELSE")
print("-"*60)
print()

a = 23
print(f"Value of a : {a}")

if a % 2 == 0:
    print(f"{a} is Even")
else:
    print(f"{a} is Odd")
# ---------------------------------------------------------
# 3. IF - ELIF - ELSE
# ---------------------------------------------------------
print("-"*60)
print("3. IF - ELIF - ELSE")
print("-"*60)
print()

marks = 78
print(f"Value of marks : {marks}")

if marks >= 90:
    print("Grade : A")
elif marks >= 75:
    print("Grade : B")
elif marks >= 60:
    print("Grade : C")
elif marks >= 40:
    print("Grade : D")
else:
    print("Grade : Fail")
# ---------------------------------------------------------
# 4. NESTED IF
# ---------------------------------------------------------
print("-"*60)
print("4. NESTED IF")
print("-"*60)
print()

age = 20
citizen = True
print(f"Value of age : {age}")
print(f"Value of citizen : {citizen}")

if age >= 18:
    print("Age is 18 or above")
    if citizen:
        print("Eligible to Vote")
    else:
        print("Not Eligible to Vote (not a citizen)")
else:
    print("Not Eligible to Vote (under age)")
# ---------------------------------------------------------
# 5. TERNARY / CONDITIONAL EXPRESSION
# ---------------------------------------------------------
print("-"*60)
print("5. TERNARY / CONDITIONAL EXPRESSION")
print("-"*60)
print()

a = 23
b = 43
print(f"Value of a : {a}")
print(f"Value of b : {b}")

print(f"result = \"a is bigger\" if a > b else \"b is bigger\"")
result = "a is bigger" if a > b else "b is bigger"
print(f"{result}")
# ---------------------------------------------------------
# 6. IF WITH LOGICAL OPERATORS
# ---------------------------------------------------------
print("-"*60)
print("6. IF WITH LOGICAL OPERATORS")
print("-"*60)
print()

a = 23
b = 43
print(f"Value of a : {a}")
print(f"Value of b : {b}")

if a > 10 and b > 10:
    print("Both a and b are greater than 10")
print()

if a > 30 or b > 30:
    print("At least one of a or b is greater than 30")
print()

if not (a > 30):
    print("a is NOT greater than 30")
# ---------------------------------------------------------
# 7. PASS STATEMENT
# ---------------------------------------------------------
print("-"*60)
print("7. PASS STATEMENT")
print("-"*60)
print()

a = 23
print(f"Value of a : {a}")

if a > 10:
    pass    # do nothing yet, placeholder for future code
print("pass statement used (no output from if block)")