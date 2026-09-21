# =============================================
# OOPS : CLASSES
# =============================================

print("="*60)
print("4. ACCESSING ATTRIBUTES USING OBJECT")
print("="*60)
print()


class Bag:
    material = "Leather"
    zips = 3
    pockets = 2


reebok = Bag()

print(f"Reebok Material : {reebok.material}") # "OBJECT".ATTRIBUTE
print(f"Reebok Zips     : {reebok.zips}")
print(f"Reebok Pockets  : {reebok.pockets}")
print()