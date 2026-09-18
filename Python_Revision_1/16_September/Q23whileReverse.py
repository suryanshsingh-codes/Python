# 2. REVERSE A NUMBER
print("2. REVERSE A NUMBER")
print()

number = 12345
print(f"Value of number : {number}")
print()

reverse = 0
while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10
print(f"Reversed : {reverse}")
print()
