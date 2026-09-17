print("\n-------->Starting My Python Journey Now : DAY 5 : File Hadnling, OOPs, Dunder methods, Args and Kwargs, Decorators<--------\n")

print(".......EXCEPTION HANDLING........")
# Creating, Readind, Writting a file
file1=open(r"FileHandling1.txt") # open a file in specified mode
print(file1.read()) #read a file by opening it
print("\n")
file1.close()

file2=open("FileHandling2.txt","w") # open a file in specified mode
file2.write("This is the new file which I created.")
file2.close()

file2=open("FileHandling2.txt","r") # open a file in specified mode
print(file2.read()) #read a file by opening it
file2.close()
print("\n")


print(".....OBJECT ORIENTNED PROGRAMMING......")
# Generally oops is used in management systems

# creating classes
class myClass1:
    
    
    a=5 # vairable inside a class is attribute
    def sayHello(self): # fucntion inside a class become a method
        print("hello everyone, i am first class.")

#creating object for this class
class1=myClass1() # instance of this class is object
print(class1.a, " is the class variable = attribute")
class1.sayHello()
print("\n")


# (self) and connection of object and classes
#CONSTRUCTORS: run automatically when object created, take the parameteres of class, target object location
class myClass2:
    def __init__(self, age, name): # self is targetting location of myclass2
        self.age=age
        self.name=name
        
    def printAttrubutes(self): # instance mehod becaue self is used and self -> object
        print(f"The Age of the student is : - {self.age}")
        print(f"The name of the student is : - {self.name}")

    # decorators-> class method: used for classes, cannot acces attributes through class like cls.age
    @classmethod
    def hello(cls): #cls will target the class location 
        print(f"hello, I am class method and cannot acces attributes through like myClass2.age, self.age, cls.age")

    # decorators-> static method: does not target any class or object location and act like a normal function accessed directly by class and stay common for all the objects
    @staticmethod
    def helloObject():
        print(f"hello, I am static method and cannot acces attributes through like myClass2.age, self.age, cls.age")

class2=myClass2(24,"Surya") # taking the parameters of class
print(class2.age, " is the value of age i have given")
print(class2.name, " is the value of name i have given")
class2.printAttrubutes()

class2.hello() # class method through object
myClass2.hello() # class method through class

class2.helloObject() # static method through object
myClass2.helloObject() # static method through class
print("\n")


# INHERITANCE
print("....Inheritance Example....")
class Animal: # parent class
    def __init__(self, name):
        self.name=name
        
    def show(self):
        print(f"Hello, my animal name is : {self.name} and age is : {self.age}") #this age will execute only by child: human class, but if animal access it, error wil be raised

class Human(Animal): # way to inherit another class, child class
    def __init__(self, name, age): # humans can tell their age but animals can't
        super().__init__(name) # super function target parent class: animal
        self.age=age # age is not in animal class but it is in human so initialize it here

animal1=Animal("Dog")
print("Now i am animal class which is parent")

human1=Human("Harry", 34)
print("Now i am human class which is child")
human1.show()
print("\n")

# POLYMORPHISM
print(".......POLYMORPHISM.........")
    # standard Example
print("Printing a standard example : -  ")
def showme():
    print("I am good.")
def showme():
    print("I am the best.")
showme()# over rided so the latest one will be called

    # polymorphism example
print("Printing a proper example : -  ")
class Animal:
    def show(self):
        print("new show function")
class Human(Animal):
    def show(self):
        print("latest show function") # this method has been over rided
human1=Human()
human1.show()

    #Duck Typing  example
print("Printing a Duck Typing example : -  ")
class Seeta:
    def talk(self):
        print("Talk function of Seeta class")
class Geeta:
    def talk(self):
        print("Talk function of Geeta class")

obj1=Seeta()
obj1.talk()
obj2=Geeta()
obj2.talk()
print("\n")

# ENCAPSULATION
print(".......Encapsulation............")
class Factory:
    a="pune"  # this is public: accesed inside class and outside class
    # in python protected=private
    _b="okhla" # this is protected
    __c="lokhandwala" # this is private: accessed inside class but not outside class
    def show(self):
        print(self.a, " is a public")
    def show2(self):
        print(self._b, " is a protected")
    def show3(self):
        print(self.__c, " is private")
class SugarcanMill(Factory):
    pass

print("\n")
print("by the parent class: - ")
myObj=Factory()
myObj.show()
myObj.show2()
myObj.show3()
print("\n")
print("by the child class: - ")
myObj2=SugarcanMill()
myObj2.show()
myObj2.show2()
myObj2.show3()
    
print("\n")
# ABSTRACTION
print(".......ABSTRACTION............\n")
from abc import ABC, abstractmethod
class Father:
    @abstractmethod # a mehod that is defined but not implemented
    def makesound(self):
        pass
class Child(Father):
    def makesound(self): # abstract method must be override
        print("I am the make sound function which has applied abstract method")
c=Child()
c.makesound()

#DUNDER METHOD: customize behaviour of class, make your class and object behave like built-in data type
print(".......DUNDER METHODS............\n")
class Harry:
    def __init__(self, name):
        self.name=name
    def __str__(self): # this dunder method will execute by : print(obj), because while printing the "OBJ" it access the dunder method __str__ directly
        return f"i am __str__ dunder method and you will get me by printing the direct {self.name} object" # you have to return tha value
    
    def __add__(self, other): # to add two objects
        return f"your combined name is {self.name + other.name}"

obj=Harry("coder")
obj2=Harry(" hacker")
print(obj) # operate on dunder method __str__:  make your class and object behave like built-in data type
print(obj+obj2) # FOR TWO OBJECTS operate on dunder method __add__:  make your class and object behave like built-in data type

#Dunder Methods  example
print("\nPrinting a Dunder Methods example of three objects : -")
class Harry:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"i am __str__ dunder method and you will get me by printing the direct {self.name} object"
    
    def __add__(self, other):
        sum=0
        for i in other: # adding the age value
            sum+=i.age
        return f"your combined age is {self.age + sum}\n"

obj=Harry("coder",12)
obj2=Harry(" hacker",12)
obj3=Harry("developer",12)
print(obj) # another way to print the __str__ dunder method to print object
print(obj+(obj2,obj3))


#DECORATOROS
print("..........DECORATORS.........\n")
print("\nPrinting a Built-In Decorators example of  : - \n ")
class Animal:
    @property
    def show(self):
        print("hello, i am a function inside a function below decorators")
obj=Animal()
obj.show # now this must be called without parethesis

    #USER DEFINED DECORATOR: is a function modifying a function without changing the function
print("\nPrinting a User Defined Decorators example of  : -")
def decorate(myFucntion):
    def wrapper(a,b):
        print("I will print myself before the function hello")
        myFucntion(a,b)
        print("I will print after the funciton")
    return wrapper

@decorate
def addFunction(a,b):
    print(f"Your total is {a+b}")
addFunction(2,3)


#ARGS AND KWARGS
print("..........ARGS AND KWARGS...........\n")

def addition(*args):
    print(*args, " display all the numbers together, using single parameter\n")
addition(232,322,4,324,234,32,423,43)

def addition(*args):
    sum=0
    for i in args:
        sum+=i
    print(sum, " using a single parameter to take multiple arguement and add them\n")
addition(232,322)

def addition(**kwargs):
    print(kwargs, " just using keyword arguement to assign multiple arguments using a single parameter\n")
addition(a=32,b=323)