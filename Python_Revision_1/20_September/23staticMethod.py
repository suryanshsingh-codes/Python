# =============================================
# OOPS : STATIC METHOD
# =============================================

print("="*60)
print("5. STATIC METHOD")
print("="*60)
print()


class Bag:
    # STATIC METHOD : ACTS LIKE REGULAR FUNCTION
    @staticmethod
    def showDetails():
        print("This is a Static Method")
        print("It does not access class or instance")


Bag.showDetails()
print()