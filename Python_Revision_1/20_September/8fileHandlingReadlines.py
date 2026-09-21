# =============================================
# 7. readlines() — WITHOUT 'with'
# =============================================
print("="*60)
print("7. readlines() — WITHOUT 'with'")
print("="*60)
print()

file = open("demo.txt", "r")
lines = file.readlines()
print(f"Total lines : {len(lines)}")
for i in range(len(lines)):
    print(f"Line {i+1} : {lines[i].strip()}")
file.close()
print()