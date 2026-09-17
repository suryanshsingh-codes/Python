# 1. COMMENTS

"""This will be my multililne comment and I am going to revise my Python"""
# This will be my single line comment and I am going to revise my Python

print("\n-------->Starting My Python Journey Now: DAY 1: Basics, Conditonals, Loops<--------\n")

# 2. VARIABLES
    # Variable
myVar1=23
myVar2="Suryansh Singh"

# CHARCTER AND UNICODE CONVERSION
a="A"
b=98
print(ord(a)) # converts into the number
print(chr(b)) # converts into the string

# 3. TYPES OF VARIABLES
print(type(myVar1), f"is the type of my variable : myVar1= {myVar1}")
print(type(myVar2), f"is the type of my variable : myVar2= {myVar2}\n")

# 4. STRING SLICING
print(myVar2[2:10:2], f"is now my sliced string of {myVar2}\n")

# 5. TYPE CONVERSION
    # EXPLICIT TYPE CONVERSION
myVar3=float(myVar1)
print(myVar3, f" here i have done implicit type conversion of Integer: {myVar1} to Float: {myVar3}")
    # IMPLICIT TYPE CONVERSION
print(25.8/myVar1, f" here explicit type conversion of dividing float:25.8 by Integer: {myVar1}\n")

# 6. TAKING INPUT FROM THE USER
myInput1=int(input("Enter Your Input Number: "))
print(myInput1, " was your Input\n")

# 7. ARITHMATIC FUNCTIONS
myVar4=21
print(myVar1+myVar4, ": is the +  of two numbers")
print(myVar1-myVar4, ": is the -  of two numbers")
print(myVar1*myVar4, ": is the *  of two numbers")
print(myVar1/myVar4, ": is the /  of two numbers")
print(myVar1//myVar4, ": is the //  of two numbers")
print(myVar1%myVar4, ": is the %  of two numbers")
print(myVar1**myVar4, ": is the **  of two numbers\m\n")

# 8. OPERATORS
    # ASSIGNMENT OPERATOR
        # also a example of FORMATTED STRINGab
print(f"myVar1: {myVar1}, i have assigned the given value to variable.")
myVar1+=10
    # COMPOUND ASSIGNMENT OPERATOR
print(f"myVar1: {myVar1}, i have re- assigned the variable using +=.")
myVar1-=10
print(f"myVar1: {myVar1}, i have re- assigned the variable using -=.\n")
    # COMPARISION OPERATOR
print(myVar1==myVar4, f" is the == comparision of {myVar1} and {myVar4}")
print(myVar1<myVar4, f" is the < comparision of {myVar1} and {myVar4}")
print(myVar1>myVar4, f" is the > comparision of {myVar1} and {myVar4}")
print(myVar1>=myVar4, f" is the >= comparision of {myVar1} and {myVar4}")
print(myVar1<=myVar4, f" is the <= comparision of {myVar4} and {myVar4}")
print(ord("A")," is the ascii value of A")
print(ord("z")," is the ascii value of z")
print("A"=="z", f" is the string comparision of A and z\n")
    # LOGICAL OPERATOR
print(myVar1<myVar4 and 34==34,f" is the and comparison of {myVar1}<{myVar4} and 34==34" )
print(myVar1<myVar4 or 34==34,f" is the or comparison of {myVar1}<{myVar4} and 34==34\n" )

# 9. CONDITIONAL STATEMENTS
if myVar4>myVar1:
    print(f"{myVar4}> {myVar1}: this was done, then {myVar4} is greater")
elif myVar4>0:
    print(f"the elif condition executed because: {myVar4}>0 ")
else:
    print(f"{myVar4}> {myVar1}: this was done, then {myVar1} is greater")

# 10. LOOPS
    # FOR LOOP
for i in range(20,0,-3):
    print("My for Loop statement:  ",i)
    # WHILE LOOP
while myVar1>=0:
    print("My While Loop statement:  ", myVar1)
    myVar1-=5