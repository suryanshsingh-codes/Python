print("\n-------->Starting My Python Journey Now : DAY 5 : List, Set and Dictionary Comprehensions<--------\n")

print(".......List Comprehension........")
myList=[i for i in range(1,21) if i%2==0]
print(myList)
print("\n") 

print(".......Dictionary Comprehension........")
myDict={ i : i**2 for i in range( 1,11)}
print(myDict)
print("\n") 


print(".......Set Comprehension........")
mySet=(i for i in range(1,21) if i%2==0)
print(mySet)
print("\n") 


print(".......Lambda Function........")
# lambda function: used for only once or temporary, defined by keyword "lambda": variable= lambda inputs : calculation/output
additon=lambda a,b: a+b # this variable addition lambda will be treated as a object
print(additon(3,4)," is the result of lambda function")
print("\n") 

print(".......Map Function........")
# Lambda functions are used with map funciotns
# Map is used to apply a function to multiple line, it takes a iterable and do calculation on every object
l=[1,2,3,4,5]
result= map(lambda x:x**2, l) # we can use our function at place of lamda also
print(result) # this will print a object
print(list(result), " is the implementation of map") #converting the object into a list
print("\n") 


print(".......Filter Function..... ...")
# used to filter out a stuff and it works on TRUE and FALE
# accepts iterable, test each items and store the accepted values
l2=[1,2,3,4,5,6,7,8,9,10]
def even(x):
    if x%2==0:
        return True
    else: 
        return False
result= filter(even,l2)
print(result)
print(list(result), " is the implementation of filter\n")


print(".......Modules and Packages........")
import mathsModuleDay6
print(mathsModuleDay6.addition(45,43), " using an addition function from another module")
# or you can direct import like this
from mathsModuleDay6 import multiplication
print(multiplication(45,43), " using a multiplication function directly by importing exact function\n")