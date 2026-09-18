# 3. PALINDROMIC NUMBER CHECK
print("3. PALINDROMIC NUMBER CHECK")
print()

number = 12321
print(f"Value of number : {number}")
print()

temporary = number
reverse = 0
while temporary > 0:
    digit = temporary % 10
    reverse = reverse * 10 + digit
    temporary = temporary // 10

if number == reverse:
    print(f"{number} is a Palindrome")
else:
    print(f"{number} is NOT a Palindrome")
print()
