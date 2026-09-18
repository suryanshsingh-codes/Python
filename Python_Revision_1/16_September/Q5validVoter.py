# ---------------------------------------------------------
# Q4. VALID VOTER CHECK
# ---------------------------------------------------------
print("-"*60)
print("Q4. VALID VOTER CHECK")
print("-"*60)
print()

name = input("What's your name? ")
age = int(input("What's your age? "))
print()

print(f"Value of name : {name}")
print(f"Value of age  : {age}")
print()

if age >= 18:
    print(f"Hello {name}, you are a valid voter")
else:
    print(f"Hello {name}, you are NOT a valid voter")
print()