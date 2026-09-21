# =============================================
# EXCEPTION HANDLING
# =============================================
print("="*60)
print("EXCEPTION HANDLING")
print("="*60)
print()


# 1. WITHOUT TRY-EXCEPT (Program crash)
print("1. WITHOUT TRY-EXCEPT")
print()

a = 10
b = 0

print(f"Value of a : {a}")
print(f"Value of b : {b}")
print()

# print(a / b)   ← ye line ZeroDivisionError dega aur program crash ho jaayega
# print("Yeh line nahi chalegi")
print("(Comment hataya toh crash ho jaayega)")
print()


# 2. TRY-EXCEPT (Basic)
print("2. TRY-EXCEPT (BASIC)")
print()

a = 10
b = 0

print(f"Value of a : {a}")
print(f"Value of b : {b}")
print()

try:
    result = a / b
    print(f"Result : {result}")
except:
    print("Error aaya! Zero se divide nahi kar sakte")
print()


# 3. TRY-EXCEPT WITH SPECIFIC EXCEPTION
print("3. TRY-EXCEPT (SPECIFIC EXCEPTION)")
print()

a = 10
b = 0

print(f"Value of a : {a}")
print(f"Value of b : {b}")
print()

try:
    result = a / b
    print(f"Result : {result}")
except ZeroDivisionError:
    print("ZeroDivisionError : Zero se divide nahi kar sakte")
print()


# 4. TRY-EXCEPT-ELSE
print("4. TRY-EXCEPT-ELSE")
print()

a = 10
b = 2

print(f"Value of a : {a}")
print(f"Value of b : {b}")
print()

try:
    result = a / b
except ZeroDivisionError:
    print("ZeroDivisionError : Zero se divide nahi kar sakte")
else:
    print(f"Result : {result}")
    print("(else chala kyunki koi exception nahi aaya)")
print()


# 5. TRY-EXCEPT-FINALLY
print("5. TRY-EXCEPT-FINALLY")
print()

a = 10
b = 0

print(f"Value of a : {a}")
print(f"Value of b : {b}")
print()

try:
    result = a / b
    print(f"Result : {result}")
except ZeroDivisionError:
    print("ZeroDivisionError : Zero se divide nahi kar sakte")
finally:
    print("(finally hamesha chalega — exception ho ya na ho)")
print()


# 6. MULTIPLE EXCEPTIONS
print("6. MULTIPLE EXCEPTIONS")
print()

a = 10
b = "abc"

print(f"Value of a : {a}")
print(f"Value of b : {b}")
print()

try:
    result = a / b
    print(f"Result : {result}")
except ZeroDivisionError:
    print("ZeroDivisionError : Zero se divide nahi kar sakte")
except TypeError:
    print("TypeError : Galat type ke saath operation nahi kar sakte")
print()


# 7. RAISE (Manually throw exception)
print("7. RAISE")
print()

age = -5
print(f"Value of age : {age}")
print()

try:
    if age < 0:
        raise ValueError("Age negative nahi ho sakti")
    print(f"Age : {age}")
except ValueError as error:
    print(f"ValueError : {error}")
print()