# =============================================
# 1. WRITE MODE ('w') — WITHOUT 'with'
# =============================================
print("="*60)
print("1. WRITE MODE ('w') — WITHOUT 'with'")
print("="*60)
print()

file = open("demo.txt", "w")
file.write("Hello Surya\n")
file.write("Welcome to File Handling\n")
file.write("Python is awesome\n")
file.close()

print("File 'demo.txt' written successfully")
print()