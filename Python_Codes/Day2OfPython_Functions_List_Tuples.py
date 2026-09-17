print("\n-------->Starting My Python Journey Now : DAY 2 Functions, List, Tuples<--------\n")
# 1. FUCNTIONS
def myAddFun1(a,b,c=23):
    print(a+b+c, f"is the sum of the numbers {a} and {b} and This function has PARAMETER and NO RETURN VALUE")
myAddFun1(25,23,c=100)

def myAddFun2(a,b,c=23):
    return(f"{a+b+c} is the sum of the numbers {a} and {b}")
myAddFun1Value=myAddFun2(25,23)
print(myAddFun1Value, "This function has PARAMETER and RETURN VALUE\n")

def myGreetFun1():
    print("I am practicing my Python Coding and This function has NO PARAMETER and NO RETURN VALUE")
myGreetFun1()

def myGreetFun2(SayHi):
    return (f"{SayHi} I am practicing my Python Coding")
myGreetFun1Value= myGreetFun2(SayHi="Hello")
print(myGreetFun1Value, "This function has NO PARAMETER and RETURN VALUE\n")

# 2. DATA STRUCTURES
    # 1. List
myList1=[1,3,4,4,5,6,7,8,9]

print(f"{myList1} is my myList")
myList1.append(2)
print(myList1, ": 2 is appended in my myList")

myList1.insert(3,233)
print(myList1, ": 3, 233 is now inserted into myList" )

myList1.extend([2,3,434,3,4,34,343,4,23])
print(myList1, ": [2,3,434,3,4,34,343,4,23] is now extended")

myList1.remove(434)
print(myList1, ": 434 is now removed from myList")

myList2=myList1.pop(5)
print(myList2, " is popped")

myList3=myList1.index(34)
print(myList3, " : 34 index is accesed")

c=myList1.count(434)
print(c, " is the frequency of 434")

myList1.sort()
print(myList1, " is the sorted myList")

myList1.reverse()
print(myList1, " is the revered myList")

myList4=myList1.copy()
print(myList4, " shallow copy created of myList\n")

        #  LIST TRAVERSING
            # USING INDEX
for i in range(len(myList1)):
    print(myList1[i], f" is the {i}th element of my list")
print("\n")
            # DIRECTLY ON LIST
for i in myList1:
    print(i, f" element of my list")
print("\n")

    # 2. TUPLES
myTuple1=(2,3,432,42,42,3)
print(myTuple1, " is my Tuple")
countTuple=myTuple1.count(42)
indexElement=t=myTuple1.index(42)
print(countTuple, " is the frequency.",indexElement," is the first index of 42\n")

        #  TUPLE TRAVERSING
            # USING INDEX
for i in range(len(myTuple1)):
    print(myTuple1[i], f" is the {i}th element of my Tuple")
print("\n")
            # DIRECTLY ON TUPLE
for i in myTuple1:
    print(i, f" element of my Tuple")
    
print("\n")

        # TUPLE UNPACKING
myTuple2,myTuple3,myTuple4=(223,324,2423)
print(myTuple2,myTuple3,myTuple4, ": These are tuple Unpacking")