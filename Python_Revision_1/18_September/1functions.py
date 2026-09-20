# =============================================
# FUNCTIONS 
# =============================================
print("="*60)
print("FUNCTIONS ")
print("="*60)
print() # this print() is also a function : built - in function

# ----------------------------------------
# CREATING OWN FUNCTION - USER DEFINED FN()
# ----------------------------------------

print("----------CREATING OWN FUNCTION - USER DEFINED FN()----------")

print("1. creating hello() function")
def hello():
    print("Hello, i was created by user")
hello()
print()


print("2. creating sum() function + using parameters")
def sum(a,b):
    print(f"The sum of {a} and {b} that you provided = {a+b}")
sum(34,343)
print()
print()



# =============================================
# TYPES OF ARGUMENTS
# =============================================
print("----------TYPES OF ARGUMENTS----------")
print()

# ----------------------------------------
# 1. POSITIONAL ARGUMENT
# ----------------------------------------
print("1. POSITIONAL ARGUMENT")
# values are passed in the SAME ORDER as parameters
def printDetails(name, age, domain):
    print(f"Name = {name} | Age = {age} | Domain = {domain}")
# 34 goes to name , 43 goes to age , "AI" goes to domain
printDetails("Surya", 21, "AI")
print()


# ----------------------------------------
# 2. KEYWORD ARGUMENT
# ----------------------------------------
print("2. KEYWORD ARGUMENT")
# values are passed using the PARAMETER NAME
def printDetails(name, age, domain):
    print(f"Name = {name} | Age = {age} | Domain = {domain}")
# order does NOT matter here
printDetails(age=21, name="Surya", domain="AI")
print()


# ----------------------------------------
# 3. DEFAULT ARGUMENT
# ----------------------------------------
print("3. DEFAULT ARGUMENT")
# default value is used when NO value is passed
def sum(a, b, c=100):
    print(f"The sum of {a}, {b} and {c} = {a + b + c}")
# c uses its default value = 100
sum(34, 43)
# c is OVERRIDDEN by 2
sum(34, 43, 2)
print()
