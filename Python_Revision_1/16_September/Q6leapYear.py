# ---------------------------------------------------------
# Q5. LEAP YEAR CHECK
# ---------------------------------------------------------
print("-"*60)
print("Q5. LEAP YEAR CHECK")
print("-"*60)
print()

year = int(input("Enter a year : "))
print()

print(f"Value of year : {year}")
print()

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is NOT a Leap Year")
print()