# =============================================
# 7. SUM OF EVEN & ODD NUMBERS IN A RANGE
# =============================================
print("="*60)
print("7. SUM OF EVEN & ODD NUMBERS IN A RANGE")
print("="*60)
print()

start = int(input("Enter start : "))
end = int(input("Enter end   : "))
print()

print(f"Start : {start}")
print(f"End   : {end}")
print()

even_sum = 0
odd_sum = 0

for i in range(start, end+1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print(f"Sum of Even numbers : {even_sum}")
print(f"Sum of Odd numbers  : {odd_sum}")
print()