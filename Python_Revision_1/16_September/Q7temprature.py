# ---------------------------------------------------------
# TEMPERATURE CATEGORY (IF-ELIF LADDER)
# ---------------------------------------------------------
print("-"*60)
print("TEMPERATURE CATEGORY (IF-ELIF LADDER)")
print("-"*60)
print()

temp = float(input("Enter temperature in Celsius : "))
print()

print(f"Value of temp : {temp} °C")
print()

if temp < 0:
    print("Freezing Cold")
elif temp < 10:
    print("Very Cold")
elif temp < 20:
    print("Cold")
elif temp < 30:
    print("Pleasant")
elif temp < 40:
    print("Hot")
else:
    print("Very Hot")
print()