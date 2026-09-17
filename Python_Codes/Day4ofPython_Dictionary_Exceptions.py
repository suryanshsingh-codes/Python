print("\n-------->Starting My Python Journey Now : DAY 4 : Dictionary, Exception Handling<--------\n")
# 4. Dictionary

print("Creating a dictionary.....")
myDictionary={}
print(type(myDictionary),"is type of my data")
myDictionary={1:"hello"}
print(myDictionary, " is my dictionary\n")

print("Updating a dictionary.......")
myDictionary[1]="hello world" #updating a element
myDictionary[2]="this is mydict" #adding a new element
print(myDictionary,"is my updated dicitoanry\n")

#Accessing the element of dictionary
print(myDictionary[1],"is the example of accessing the elements\n")

# Looping of dictionaries
print("Looping on dicionaries.........")
for i in myDictionary:
    print(i,"is the element of dictionaries")
for i in myDictionary.keys():
    print(i, "is the element of dictionaries")
    
for i in myDictionary.values():
    print(i, "is the element of dictionaries")
print("\n")

#Dictionaries Methods
print("Dictionaries methods.......\n")

myDictionary2=myDictionary.copy() #creating a shallow copy of my dicionary
print(myDictionary2, "is my dictionary 2\n")

print(myDictionary.items(), " these are my diciotnary 1 items\n")#print the dictionary items

myDictionary3={4:"jkdjfsk",5:"rw5fs"}
for i in myDictionary3:
    myDictionary[i]=myDictionary3[i]
print(myDictionary, "is my dictionary after merging two dictionaries.\n")
    
print(myDictionary.get(1), " is the value for key if it is present\n")
    
myPop=myDictionary.pop(1)# remove the specified key
print(myPop,"is the pop method")
myPop2=myDictionary.popitem()# remove the key-value pair
print(myPop2,"is the pop item method\n")
    
myDictionary.clear() # this will remove all the elements from dictonaries
print(myDictionary, "is my cleared dictionary\n")











# EXCEPTION HANDLIG
print( "...........Learning the exception handling.........\n")
num1=0

    # Try - Except [ except is mandatory scope]
try:
    print(10/num1)
except ZeroDivisionError:
    print("Sorry You Cannot divide by zero.")
    
try:
    print(10/num1)
except ZeroDivisionError as err:
    print(err, " is the error it throw\n")
    
    # Try - Except - Else Block
try:
    print(10/2)
except ZeroDivisionError as err:
    print(err, " is the error it throw\n")
else:
    print("No error occured\n")
    
    # Try - Except - Else - Finally  Block
try:
    print(10/2)
except ZeroDivisionError as err:
    print(err, " is the error it throw\n")
else:
    print("No error occured")
finally:
    print("I am finally block\n")

    # Raise
age=int(input("Enter Your Age: "))
try:
    if age<10 or age>18:
        raise ValueError ("Your Age is not in the range.")
    else:
        print("Welcome")
except Exception as err:
    print(err, " is the raise error")
print("The club will start soon.\n")