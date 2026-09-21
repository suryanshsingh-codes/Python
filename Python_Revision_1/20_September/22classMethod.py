# =============================================
# OOPS : CLASS METHOD
# =============================================

print("="*60)
print("4. CLASS METHOD")
print("="*60)
print()


class Bag:
    material = "Leather"

    # CLASS METHOD : WORKS WITH CLASS ITSELF and DIRECTLY CLASS ATTRIBUTES AND METHODS 
    @classmethod
    def showMaterial(cls):
        print(f"Material : {cls.material}")

Bag.showMaterial()
print()