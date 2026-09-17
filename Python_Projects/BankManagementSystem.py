'''
Requirements: 
    bank account
    deposit money
    withdraw money
    details check
    update details
    delete account
'''
import json # to ostore user data
import random # to generate random number
import string # to use some string functionalities
from pathlib import Path # for showing files to data, we will need path
# i want to store the user data when he fills the data for creating an account, so that if i close a function, the data stay saved-> create a json file


'''
main data file = json file-> the original database
to update data = use a dummy data file->stored in list form
'''

#creating a bank class so that a new user behaves like an object
class Bank:
    '''
    main data file = json file-> the original database
    to update data = use a dummy data file->stored in list form
    '''
    database='BankUserData.json'
    data=[]
    
    #if users gives an invaild file
    try:
        # the file must exists for further opereations
        if Path(database).exists():
            # transdering main data into the dummy data file
            with open (database) as fs:
                data=json.loads(fs.read())
        else:
            print("No such files")
    except:
        print("An error occured")
        
    # a class method to save the user details in dummy data and update it to main database
    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))
    # now generate a account number
    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k = 3)
        num = random.choices(string.digits,k= 3)
        spchar = random.choices("!@#$%^&*",k = 1) #k is the number of values
        id = alpha + num + spchar
        random.shuffle(id) # this will be a list
        return "".join(id) # now list converted to string
    
    # ALL THE FUNCTIONS
    
    # 1. function to create a account
    def Createaccount(self):
        print("......CREATING ACCOUNT.........\n")
        # 1. taking user details
        info={"name": input("Tell your name :- "),
              "age" : int(input("tell your age :- ")),
              "email": input("tell your email :- "),
              "pin": int(input("tell your 4 number pin :- ")),
              "accountNo." : Bank.__accountgenerate(), # this account number will be generated randomly
              "balance" : 0}
        # 2. condition to create a account
        if info['age'] < 18  or len(str(info['pin'])) != 4:
            print("sorry you cannot create your account\n")
        else:
            print("account has been created successfully\n")
        for i in info:
            print(f"{i} : {info[i]}")
        print("please note down your account number\n")

        Bank.data.append(info)

        Bank.__update()

    # 2. function to deposit money to the accoount
    def depositmoney(self):
        print("......DEPOSITING MONEY.........\n")
        # 1. ask user the credentials
        accnumber=input("Enter your account number:- ")
        pin=int(input("Enter Your pin:- "))

        # 2. extract the matching data from main database
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        # 3. final update to data
        if userdata == False:
            print("sorry no data found\n")
        
        else:
            amount = int(input("how much you want to depoit:- "))
            if amount  > 10000 or amount < 0:
                print("sorry the amount is too much you can deposit below 10000 and above 0\n")

            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print("Amount deposited successfully\n")
        
    # 3. function to withdraaw money from the accoount
    def withdrawmoney(self):
        print("......WITHDRAW MONEY.........\n")
        
        # 1. ask user the credentials
        accnumber = input("please tell your account number:- ")
        pin = int(input("please tell your pin as well:- "))

        # 2. extract the matching data from main database
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
          # this userdata will be a dictionary inside a list, at list[0] there will be a whole dictionary
        if userdata == False:
            print("sorry no data found\n")
        
        else:
            amount = int(input("how much you want to withdraw:-"))
        if userdata[0]['balance']  < amount:
            print("soory you dont have that much money.\n")
                
        else:
                    
            userdata[0]['balance'] -= amount
            Bank.__update()
            print("Amount withdrew successfully\n")
            
    # 4. function to show details of the accoount
    def showdetails(self):
        print("......SHOW DETAILS.........\n")
        
        # 1. ask user the credentials
        accnumber = input("please tell your account number: ")
        pin = int(input("please tell your pin as well: "))

         # 2. extract the matching data from main database
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        print("your information are: \n")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")
        print("\n")
    
    # 5. function to update details of the accoount
    def updatedetails(self):
        print("......UPDATE DETAILS.........\n")
        
        # 1. ask user the credentials
        accnumber = input("please tell your account number: ")
        pin = int(input("please tell your pin as well: "))

        # 2. extract the matching data from main database
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
            # check if user data not matches
        if userdata == False:
            print("no such user found\n")
            # if data matches
        else:
            print("you cannot change the age, account number, balance")

            print("Fill the details for change or leave it empty if no change")
            # 1. asking the user a new data
            newdata = {
                "name": input("please tell new name or press enter to skip : "),
                "email":input("please tell your new Email or press enter to skip :"),
                "pin": input("enter new Pin or press enter to skip: ")
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]['name']
            if newdata["email"] == "":
                newdata["email"] = userdata[0]['email']
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]['pin']
            
            # these cannot be changed so will stay as same
            newdata['age'] = userdata[0]['age']
            newdata['accountNo.'] = userdata[0]['accountNo.']
            newdata['balance'] = userdata[0]['balance']
            
            # re-storing the pin and typecasting it to integer type
            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])
            

            for i in newdata: # accessing keys of new data
                 if newdata[i] == userdata[0][i]: # if new data and database is same
                     continue
                 else:
                     userdata[0][i] = newdata[i] # change if new data is not same as data base

            Bank.__update()
            print("details updated successfully\n")
            
    # 6. function to delete the accoount
    def Delete(self):
        print("......DELETE DETAILS.........\n")
        
        # 1. ask user the credentials
        accnumber = input("please tell your account number: ")
        pin = int(input("please tell your pin as well: "))

        # 2. extract the matching data from main database
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
            # check if user data not matches
        if userdata == False:
            print("no such user found\n")
            # if data matches
        else:
            check = input("press y if you actually want to delete the account or press n")
            if check == 'n' or check == "N":
                print("bypassed")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("account deleted successfully ")
                Bank.__update()



# Initializing the user as a object of Bank
user=Bank()

print("........BANK MANAGEMENT SYSTEM.........\n")
# Showing the user a interaction environment
print("press 1 for creating an account")
print("press 2 for Deposititing the money in the bank ")
print("press 3 for withdrawing the money ")
print("press 4 for details ")
print("press 5 for updating the details")
print("press 6 for deleting your account\n")

# Getting user response
check = int(input("tell your response :- "))
# switching on the functions of bank management data
if check == 1:
    user.Createaccount()

if check == 2:
    user.depositmoney()

if check==3:
    user.withdrawmoney()
    
if check==4:
    user.showdetails()
    
if check==5:
    user.updatedetails()
    
if check==6:
    user.Delete()