# =============================================
# OOPS : INSTANCE METHOD
# =============================================

print("="*60)
print("1. INSTANCE METHOD")
print("="*60)
print()


class Bag:
    def __init__(self, material, zips, pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets

    # INSTANCE METHOD : WORKS WITH INSTANCE : object : address : self
    def showDetails(self):
        print(f"Material : {self.material}")
        print(f"Zips     : {self.zips}")
        print(f"Pockets  : {self.pockets}")


reebok = Bag("Leather", 3, 2)
reebok.showDetails()
print()