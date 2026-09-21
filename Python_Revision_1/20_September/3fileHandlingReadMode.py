# =============================================
# 2. READ MODE ('r') — WITH 'with'
# =============================================
print("="*60)
print("2. READ MODE ('r') — WITH 'with'")
print("="*60)
print()

with open("demo.txt", "r") as file:
    content = file.read()
    print(content)
print()