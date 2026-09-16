# =============================================
# Q2. GREETING BASED ON GENDER
# =============================================
print("="*60)
print("Q2. GREETING BASED ON GENDER")
print("="*60)
print()

gender = input("Enter gender (M/F) : ").strip().upper()

print(f"Value of gender : {gender}")

if gender == "M":
    print("Good Morning Sir")
elif gender == "F":
    print("Good Morning Ma'am")
else:
    print("Invalid gender input")