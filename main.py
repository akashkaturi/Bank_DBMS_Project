
from banner import bannerPrinting
from createaccount import *
import hashlib
from existingaccount import *
from createaccount import userAccounts


# printing Banner
try:
    bannerPrinting()
except:
    print("[+] Banner Loading Failed...")
    quit()

while True:
    print()
    print("Enter 1 to Create a New Account")
    print("Enter 2 to Access an Existing Account")
    print("Enter 3 to Exit")
    userChoice = int(input())
    print()

    # creating an account
    if userChoice == 1:
        print()
        account = CreateAccount()
        account.accountCreation()
        account.sendMail()

    elif userChoice == 2:
        print()
        AccountNumber = int(input("Enter Your Account Number: "))
        ea = ExistingAccount(AccountNumber)
        # while True:
        #     password = hashlib.sha256(
        #         input("Enter Your Password: ").encode()).hexdigest()
        #     authenticationStatus = ea.authentication(password)
        #     if authenticationStatus[0] == "completed":
        #         print("3 Attempts to enter password is completed")
        #     if authenticationStatus[0] == False:
        #         print("[-] Password Incorrect..., remaining attempts: ",
        #               authenticationStatus[1])
        #     else:
        #         break
        # print()
        while True:
                password = hashlib.sha256(input("Enter Your Password: ").encode()).hexdigest()
                authenticationStatus = ea.authentication(password)
                if authenticationStatus is False:
                    print("[-] Password Incorrect...")
                else:
                    break
        print()

        if authenticationStatus == True:
            print("[+] Authentication Successful...")
            while True:
                print()
                print("Enter 1 to withdraw")
                print("Enter 2 to deposit")
                print("Enter 3 to Display Available Balance")
                print("Enter 4 to return to previous menu")
                userChoice = int(input())
                print()
                if userChoice == 1:
                    print()
                    print("Enter a Withdrawl amount")
                    withdrawlAmount = int(input())
                    ea.withdraw(withdrawlAmount)

                if userChoice == 2:
                    print()
                    depositAmount = int(input("Enter amount to Deposit: "))
                    ea.deposit(depositAmount)

                if userChoice == 3:
                    print()
                    ea.displayBalance()

                if userChoice == 4:
                    break
    elif userChoice == 3:
        quit()
