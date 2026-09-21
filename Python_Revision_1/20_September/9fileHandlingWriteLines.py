# =============================================
# 8. writelines() — WITH 'with'
# =============================================
print("="*60)
print("8. writelines() — WITH 'with'")
print("="*60)
print()

data = ["Line 1\n", "Line 2\n", "Line 3\n"]

with open("list.txt", "w") as file:
    file.writelines(data)

print("List written to file successfully")
print()