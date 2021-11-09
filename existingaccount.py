
from tkinter.constants import NONE
from createaccount import userAccounts
import hashlib
from random import randint
import smtplib
import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', passwd='abgk1234',
                               database='bank', auth_plugin='mysql_native_password',)


class ExistingAccount:

    def __init__(self, accountNumber):
        self.accountNumber = accountNumber
        self.attempt = attempt

    def userName(self):
        sql = ('select fullname from Amount where accountno=%s')
        d = (self.accountNumber,)
        x = mydb.cursor()
        x.execute(sql, d)
        uname = x.fetchone()
        return uname[0]

    def authentication(self, password):
        # while self.attempt > 0:
        #     if self.accountNumber not in userAccounts.keys():
        #         self.attempt -= 1
        #         if(self.attempt == 0):
        #             return ("completed", 1)
        #         return (False, self.attempt)

        #     elif userAccounts[self.accountNumber][0] == password:
        #         return (True, 1)
        #     else:
        #         return (False, self.attempt)
        x = mydb.cursor()
        sql = ('select password from Account where accountno=%s')
        d = (self.accountNumber,)
        x.execute(sql, d)
        pswd = x.fetchone()
        if pswd is None:
            return False
        elif pswd[0] == password:
            return True
        else:
            return False

    def withdraw(self, withdrawAmount):
        print()
        a = 'select Balance from Amount where AccountNo=%s'
        data = (self.accountNumber,)
        x = mydb.cursor()
        x.execute(a, data)
        result = x.fetchone()

        if withdrawAmount > result[0]:
            print("Insufficient Balance")
            print("Current Balance is: ", result[0])
        else:
            t = result[0] - withdrawAmount
            sql1 = ('update Amount set Balance=%s where AccountNo=%s')
            sql2 = ('update Account set Balance=%s where AccountNo=%s')
            d = (t, self.accountNumber)
            x.execute(sql1, d)
            x.execute(sql2, d)
            mydb.commit()
            print("Withdrawl Successful.")
            print(f'Amount remaining in your account is {t}')
        print()

    def deposit(self, depositAmount):
        print()
        # userAccounts[self.accountNumber][2] += depositAmount
        # print("[+] Deposit Successful...")
        a = 'select Balance from Amount where AccountNo=%s'
        data = (self.accountNumber,)
        x = mydb.cursor()
        x.execute(a, data)
        result = x.fetchone()
        t = result[0] + depositAmount
        sql1 = ('update Amount set Balance =%s where AccountNo=%s')
        sql2 = ('update Account set Balance =%s where AccountNo=%s')
        d = (t, self.accountNumber)
        x.execute(sql1, d)
        x.execute(sql2, d)
        mydb.commit()
        print('Amount Deposited')
        print(f'The current balance is {t}')
        # self.displayBalance()
        print()

    def displayBalance(self):
        # print("Available Balance: ", userAccounts[self.accountNumber][2])
        # ac = input('Enter the acc no: ')
        a = 'select * from Amount where AccountNo=%s'
        data = (self.accountNumber,)
        x = mydb.cursor()
        x.execute(a, data)
        result = x.fetchone()
        if self.accountNumber and result:
            print(f'Balance for account: {self.accountNumber} is {result[-1]}')
        else:
            print('No data')
        print()


attempt = 3
