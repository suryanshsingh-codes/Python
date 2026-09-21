# =============================================
# OOPS : ATTRIBUTES & METHODS (ALL TOGETHER)
# =============================================

print("="*60)
print("6. ATTRIBUTES & METHODS (ALL TOGETHER)")
print("="*60)
print()


class Bag:
    # CLASS ATTRIBUTE
    brand = "Reebok"

    def __init__(self, material, zips, pockets):
        # INSTANCE ATTRIBUTES
        self.material = material
        self.zips = zips
        self.pockets = pockets

    # INSTANCE METHOD
    def showDetails(self):
        print(f"Brand    : {self.brand}")
        print(f"Material : {self.material}")
        print(f"Zips     : {self.zips}")
        print(f"Pockets  : {self.pockets}")

    # CLASS METHOD
    @classmethod
    def showBrand(cls):
        print(f"Brand : {cls.brand}")

    # STATIC METHOD
    @staticmethod
    def welcomeMessage():
        print("Welcome to Bag Factory")


# CREATING OBJECT
reebok = Bag("Leather", 3, 2)

# INSTANCE METHOD CALL
print("Instance Method :")
reebok.showDetails()
print()

# CLASS METHOD CALL
print("Class Method :")
Bag.showBrand()
print()

# STATIC METHOD CALL
print("Static Method :")
Bag.welcomeMessage()
print()