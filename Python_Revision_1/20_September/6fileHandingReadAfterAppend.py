# =============================================
# 5. READ AFTER APPEND — WITHOUT 'with'
# =============================================
print("="*60)
print("5. READ AFTER APPEND — WITHOUT 'with'")
print("="*60)
print()

file = open("demo.txt", "r")
print(file.read())
file.close()
print()