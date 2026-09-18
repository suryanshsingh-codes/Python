# 1. SEPARATE EACH DIGIT OF A NUMBER
print("1. SEPARATE EACH DIGIT")
print()

number = 12345
print(f"Value of number : {number}")
print()

while number > 0:
    digit = number % 10
    print(f"Digit : {digit}")
    number = number // 10
print()