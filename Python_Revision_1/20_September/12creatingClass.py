# =============================================
# OOPS : CLASSES
# =============================================

print("="*60)
print("1. CREATING A CLASS")
print("="*60)
print()


class Bag:
    # ATTRIBUTES : VARIABLES INSIDE THE CLASS
    material = "Leather"
    zips = 3
    pockets = 2

    # METHODS : FUNCTIONS INSIDE THE CLASS
    def showDetails(self):
        print(f"Material : {self.material}")
        print(f"Zips     : {self.zips}")
        print(f"Pockets  : {self.pockets}")


print("Class 'Bag' created successfully")
print()