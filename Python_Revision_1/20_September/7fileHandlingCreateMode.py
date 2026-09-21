# =============================================
# 6. CREATE MODE ('x') — WITH 'with'
# =============================================
print("="*60)
print("6. CREATE MODE ('x') — WITH 'with'")
print("="*60)
print()

try:
    with open("newfile.txt", "x") as file:
        file.write("Newly created file\n")
    print("File 'newfile.txt' created successfully")
except FileExistsError:
    print("File already exists")
print()