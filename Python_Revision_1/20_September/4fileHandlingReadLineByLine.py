# =============================================
# 3. READ LINE BY LINE — WITHOUT 'with'
# =============================================
print("="*60)
print("3. READ LINE BY LINE — WITHOUT 'with'")
print("="*60)
print()

file = open("demo.txt", "r")
for line in file:
    print(f"Line : {line.strip()}")
file.close()
print()