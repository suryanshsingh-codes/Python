# =============================================
# OOPS : CLASSES
# =============================================

print("="*60)
print("8. CLASS WITH CONSTRUCTOR")
print("="*60)
print()


class BagFactory:
    def __init__(self, material, zips, pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def showDetails(self):
        print(f"Material : {self.material}")
        print(f"Zips     : {self.zips}")
        print(f"Pockets  : {self.pockets}")


print("Class 'BagFactory' created successfully")
print()