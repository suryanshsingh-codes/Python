# =============================================
# OOPS : CLASSES
# =============================================

print("="*60)
print("5. ACCESSING METHODS USING OBJECT")
print("="*60)
print()


class Bag:
    material = "Leather"
    zips = 3
    pockets = 2

    def showDetails(self):
        print(f"Material : {self.material}")
        print(f"Zips     : {self.zips}")
        print(f"Pockets  : {self.pockets}")


reebok = Bag()
reebok.showDetails()
print()