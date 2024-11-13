#bank App
import random
runningOn = 0
looping = 1
#DO NOT FORGET TO CHANGE THIS, 1000 IS JUST A PLACE HOLDER NUMBER

userNameList = []
userIdList =[]
userPasswordList = []
userMnyList = []
# end of place holders
#Intro/Id creation
while looping == 1:
    if(runningOn == 0):
        print("Welcome to the bank app. Select an option:\nLog In\nSign Up\nQuit")
        usrOpt = input()
        #log in
        if usrOpt == str("Log In") or usrOpt==str("1"):
           # print("LOGGING IN")
            runningOn = 1
            #signUp
        if usrOpt == str("Sign Up") or usrOpt==str("2"):
           # print("SIGNING UP")
            runningOn = 2
            #quit
        if usrOpt == str("Quit") or usrOpt==str("3"):
            #print("Quiting")
            looping = 0
        if usrOpt == str("DEBUG") or usrOpt==str("4"):
            print("DEBUGGING")
            print("WHERE DO YOU WANT TO DEBUG? \n1) LOGIN\n2) VIEW LIST")
            usrDebugOpt = input()
            if(usrDebugOpt == "1"):
                runningOn = 3
            elif(usrDebugOpt == "2"):
                print("user name list: "+ str(userNameList))
                print("user ID list: "+ str(userIdList))
                print("user Password list: "+ str(userPasswordList))
                print("user Money list: "+ str(userMnyList))
    #Login
    if(runningOn == 1):
        #check if the user id is in the list and get the list number of that
        print("Enter User ID")
        inpLoginNum = input()
        if(inpLoginNum in userIdList):
            getUsrNum = userIdList.index(inpLoginNum)
            print(getUsrNum)
            print("Enter Password")
            inpPswNum = input()
            if(userPasswordList[getUsrNum] == inpPswNum):
                print("Logging in")
                runningOn = 3
            else:
                print("Password incorrect\n")
                runningOn = 0
        else:
            print("That Id Number Does Not Exist")
            runningOn = 0
        # checks if the password of that id matches
            
    #Sign Up
    if(runningOn == 2):
        #enter useres name
        print("Enter name:")
        userName = input()
        #gives user a number
        createUserNum = random.randrange(100000, 999999)
        userCreateID = str(createUserNum)
        print("Id: " + userCreateID)
        #creates and double checks password
        passwordCheck = 0
        while(passwordCheck == 0):
            print("Create Password:")
            passwordCreate = input()
            print("Re-enter password")
            reEnterPassword = input()
        #checks if the user password is correct else have them re enterpassword
            
        
            if(passwordCreate == reEnterPassword):
                print("A minimum of $100 must be added to create an account\n1)Confirm\n2)Decline")
                usrCreateAccount = input()
                if(usrCreateAccount == "1"):
                    passwordCheck = 1
                    print("Sucess, Taking you Back to the Log In Page\n")
                    runningOn = 0
                    userPasswordList.append(reEnterPassword)
                    userIdList.append(userCreateID)
                    userNameList.append(userName)
                    userMnyList.append(100)
                else:
                    print("Okay deleting account")
                    runningOn = 0
                    passwordCheck = 1

                
            else:
                print("The password does not match, try again")
    #Logged In
    while(runningOn == 3):
        
        
        #options while logged in
        print("\nWelcome " + userNameList[getUsrNum] + "   ID NUmber: " + userIdList[getUsrNum] )
        print("Money In Account: $" + str(userMnyList[getUsrNum]))
        print("what would you like to do?\n1)WithDrawl\n2)Deposit\n3)Log out")
        usrLogInOpt = input()
    #withdrawl
        if(usrLogInOpt == 1) or (usrLogInOpt == str("1")):

            print("you have $" + str(userMnyList[getUsrNum]))
            print("How much would you like to withdrawl")
            amtToWithdrl = input()
            AmtTtlAft = int(userMnyList[getUsrNum]) - int(amtToWithdrl)
            
            if int(AmtTtlAft) < 0:
                print("You cannot withdrawl this amount\n")
            else:
                print("Withdrawling Amount")
                userMnyList[getUsrNum] -= int(amtToWithdrl)
    #deposit
        if(usrLogInOpt == 2) or (usrLogInOpt == str("2")):
            print("you have $" + str(userMnyList[getUsrNum]))
            print("How much would you like to deposit")
            amtToDepo = input()
            userMnyList[getUsrNum] += int(amtToDepo)
    #Log Out
        if(usrLogInOpt == str("3")) or (usrLogInOpt == str("3")):
            print("Logging out\n")
            runningOn = 0

