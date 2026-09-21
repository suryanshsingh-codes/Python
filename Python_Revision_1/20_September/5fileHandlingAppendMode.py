# =============================================
# 4. APPEND MODE ('a') — WITH 'with'
# =============================================
print("="*60)
print("4. APPEND MODE ('a') — WITH 'with'")
print("="*60)
print()

with open("demo.txt", "a") as file:
    file.write("This line was appended later\n")

print("New line appended successfully")
print()