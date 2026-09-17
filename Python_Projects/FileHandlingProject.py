# we want to do CRUD operation to user, and show files and folders to users 
# for which i will use a path library and cretae a function
from pathlib import Path
import os # use os to delte a file

# Creating a fileAndFolderReading function to display all files to user
def readFileAndFolder():
    path=Path('') # to read the path of current directory
    items=path.rglob("*") # Recursive glob fucntion: recursively read and provide all the elements of current directory
    for i,items in enumerate(items):# in any list we have index and value, to save both separately we use enumerate
        print(f"{i+1} : {items}") # this will give all the files and folders existing into my current directory
print("\n")

# Creating a FileCreating function
def createFile():
    
    try: # what if usr entered a invaild file
    
        readFileAndFolder() # because creating a file,i want to display existing files and folders to users
        name=input("Now, please tell your file name: ") # ask user to tell his file name
        p=Path(name) # include name of user's file into path
        
        if not p.exists() and p.is_file(): # create file only if it do not exists already
            with open(p,"w") as fs: # to open a file 
                data=input("what do you want to write into this file: ")
                fs.write(data)
            print("File Created Succesfully\n")
        else:
            print("File Exists Already.\n")
    except Exception as err:
        print(err, " is the error that occured\n")


# create a fileReading Function
def readFile():
    
    try: # what if usr entered a invaild file
        
    
        readFileAndFolder() # because creating a file,i want to display existing files and folders to users
        name=input("Now, please tell your file name: ") # ask user to tell his file name
        p=Path(name) # include name of user's file into path
        
        if p.exists() and p.is_file(): # create file only if it do not exists already
            with open(p,"r") as fs: # to open a file 
                data=fs.read()
                print(data)
            print("File Read Succesfully\n")
        else:
                print("No such file exists.\n")
    except Exception as err:
        print(err, " is the error that occured\n")



# create a fileUpdate Function-> namechange, append, overwrite
def updateFile():
    
    try: # what if usr entered a invaild file
        
    
        readFileAndFolder() # because creating a file,i want to display existing files and folders to users
        name=input("Now, please tell your file name: ") # ask user to tell his file name
        p=Path(name) # include name of user's file into path
        
        if p.exists() and p.is_file(): # what to user want to update
            print("Press 1 for Changing the Name of your Filie")
            print("Press 2 for Overwritting the data in your Filie")
            print("Press 3 for Appending the data to your Filie\n")
            result=int(input("Tell me Your Response: "))
            
            if result==1:
                name2=input("Enter Your new file name: ") # taking file name
                p2=Path(name2) # creating passing the new path 
                p.rename(p2) # renaming it
                
            if result==2:
                with open(p,"w") as fs: # to open a file 
                    data=input("Tell me that what do you want to overwrite")
                    fs.write(data)
                    
            if result==3:
                with open(p,"a") as fs: # to open a file 
                    data=input("Tell me that what do you want to append")
                    fs.write(data)
                
            print("File Updated Succesfully\n")
            
        else:
                print("File Not Exists.\n")
                
    except Exception as err:
        print(err, " is the error that occured\n")
        

# create a fileDeleting Function
def deleteFile():
    
    try: # what if usr entered a invaild file
        
    
        readFileAndFolder() # because creating a file,i want to display existing files and folders to users
        name=input("Now, please tell your file name which you want to delte: ") # ask user to tell his file name
        p=Path(name) # include name of user's file into path
        
        if p.exists() and p.is_file(): # create file only if it do not exists already
            os.remove(p)
            print("File Deleted Succesfully\n")
        else:
            print("No such file exists.\n")
    except Exception as err:
        print(err, " is the error that occured\n")


# Asks the user what he wants to interact with
print("Press 1 for creating a File")
print("Press 2 for Reading a File")
print("Press 3 for Updating a File")
print("Press 4 for Deleting a File\n")

# Accept the input
check=int(input("Enter Your Response: "))

# Working on All inputs
if check==1:
    createFile()
if check==2:
    readFile()
if check==3:
    updateFile()
if check==4:
    deleteFile()
