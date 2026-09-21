# =============================================
# OOPS : CLASSES
# =============================================

print("="*60)
print("7. OBJECT CAN MODIFY ITS OWN ATTRIBUTES")
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

campus.material = "Canvas"
campus.zips = 2
campus.pockets = 4

print("Campus Bag (After Modification) :")
campus.showDetails()
print()

print("Reebok Bag (Unchanged) :")
reebok.showDetails()
print()