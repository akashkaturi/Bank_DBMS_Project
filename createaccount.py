import hashlib
from random import randint
import smtplib
# %%
import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', passwd='abgk1234',
                               database='bank', auth_plugin='mysql_native_password',)


# account creation

userAccounts = {}


class CreateAccount:
    def genderValidation(self):
        while 1:
            self.gender = input("Please Enter Your Gender [M/F/O]: ").lower()
            if self.gender == 'm' or self.gender == 'f' or self.gender == 'o':
                return self.gender
            else:
                print("[-] Please Enter specified Gender Types Only...")
                continue

    def mobileNumValidation(self):
        while 1:
            self.mobileNo = input("Please Enter Your Mobile Number: ")
            if len(self.mobileNo) == 10:
                return self.mobileNo
            else:
                print("[-] Please Specify Your 10 digit Mobile Number: ")
                continue

    def emailValidation(self):
        while 1:
            self.email = input("Please Enter Your Gmail Address: ")
            if self.email[-10:] == "@gmail.com":
                return self.email
            else:
                print("[-] Please Enter valid Gmail Address... ")
                continue

    def passwordValidation(self):
        while -1:
            self.send_to_user_password = input("Please Type a Password: ")
            self.password = hashlib.sha256(self.send_to_user_password.encode()).hexdigest()
            self.confirmPassword = hashlib.sha256(
                input("Please Re-Type Your Password: ").encode()).hexdigest()
            if self.password == self.confirmPassword:
                return self.password
            else:
                print("[-] Password and Confirm Password Do not match try again....")
                continue

    def initialDepositAmount(self):
        while True:
            self.initialDeposit = int(input("Enter your Initial Deposit: "))
            if self.initialDeposit > 1000:
                return self.initialDeposit
            else:
                print("[-] Please Deposit Amount Greater than INR 1000...")
                continue

    # Creating Account Number
    def accountNumberGeneration(self):
        self.accountNumber = randint(10000000, 99999999)
        print("[+] Your Account Created Succesfully...")
        print("Your Account Number is: ", self.accountNumber)
        return self.accountNumber

    def updateDict(self):
        userAccounts[self.accountNumber] = [self.password, self.email, self.balance,
                                            self.name, self.mobileNo, self.aadhar, self.dob, self.gender]

        data1 = (self.accountNumber, self.fname, self.lname, self.gender, self.dob,
                 self.mobileNo, self.aadhar, self.email, self.password, self.balance)
        data2 = (self.accountNumber, self.name, self.balance)
        sql1 = ('insert into Account values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)')
        sql2 = ('insert into Amount values (%s,%s,%s)')
        x = mydb.cursor()
        x.execute(sql1, data1)
        x.execute(sql2, data2)
        mydb.commit()
        print('Data Entered Successfully...')

    def accountCreation(self):
        self.fname = input("Please Enter Your First Name: ")
        self.lname = input("Please Enter Your Last Name: ")
        self.name = self.fname + ' ' + self.lname
        self.gender = self.genderValidation()
        self.dob = input(
            "Please Enter Your Date Of Birth in [DD/MM/YYYY] format: ")
        self.mobileNo = self.mobileNumValidation()
        self.aadhar = input("Please Enter Your Aadhar Card Number: ")
        self.email = self.emailValidation()
        self.password = self.passwordValidation()
        self.balance = self.initialDepositAmount()
        self.accountNumber = self.accountNumberGeneration()
        self.updateDict()

    def sendMail(self):
        self.senderMail = 'akashkaturi7@gmail.com'
        self.pswd = 'naniabgk2'
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.ehlo()
            server.starttls()
            server.login(self.senderMail, self.pswd)
            message = 'Subject: {}\n\n{}'.format(
                'Your Account is Created', f"Welcome to FLM Bank ,Thanks {self.name} for using our services. Your Account Has Been Successfully Created. Your Account Number is: {self.accountNumber},Your Password is {self.send_to_user_password}")
            server.sendmail(self.senderMail, self.email, message)
            server.quit()
