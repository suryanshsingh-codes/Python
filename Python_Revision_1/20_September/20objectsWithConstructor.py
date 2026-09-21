# =============================================
# OOPS : CLASSES
# =============================================

print("="*60)
print("9. CREATING OBJECTS WITH CONSTRUCTOR")
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


reebokBag = BagFactory("Leather", 3, 2)
print("Reebok Bag Details :")
reebokBag.showDetails()
print()

campusBag = BagFactory("Canvas", 2, 4)
print("Campus Bag Details :")
campusBag.showDetails()
print()

skybag = BagFactory("Nylon", 4, 3)
print("Skybag Details :")
skybag.showDetails()
print()