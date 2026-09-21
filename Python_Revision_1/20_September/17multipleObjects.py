# =============================================
# OOPS : CLASSES
# =============================================

print("="*60)
print("6. MULTIPLE OBJECTS FROM SAME CLASS")
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
campus = Bag()

print("Reebok Bag Details :")
reebok.showDetails()
print()

print("Campus Bag Details :")
campus.showDetails()
print()