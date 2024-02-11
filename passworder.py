import os
import ctypes
from colorama import *
from sys import platform
import time
import getpass
import random

code = ''

def main():
    global code
    ctypes.windll.kernel32.SetConsoleTitleW("Password Manager 🔐 | Access Denied ❌")
    os.system("cls")
    print(Fore.RED + "Password Manager | By Morozov")
    password = getpass.getpass("Please write password: ")
    if password == code:
        os.system("cls")
        print(Fore.RED + "\nChecking password...")
        ctypes.windll.kernel32.SetConsoleTitleW("Password Manager 🔐 | Checking password... ⏳")
        time.sleep(1)
        ctypes.windll.kernel32.SetConsoleTitleW("Password Manager 🔐 | Access Granted ✔")
        # timer(60)
        if platform == 'win32':
            os.system("cls")
        
        else:
            os.system("exit")

        print(Fore.GREEN + "Password Manager | By Morozov\n\n[1] Google Accounts\n\n[2] Vkontakte\n\n[3] GitHub\n\n[4] Instagram\n\n[5] Password Generator\n\n[6] Exit")
        choice_option()

    else:
        os.system("cls")
        print(Fore.RED + "\nChecking password...")
        ctypes.windll.kernel32.SetConsoleTitleW("Password Manager 🔐 | Checking password... ⏳")
        time.sleep(1)
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("Password Manager 🔐 | Wrong Password ❌")
        print(Fore.RED, "\nWrong Password!")
        time.sleep(1)
        os.system("cls")
        main()
        # os.system("exit")

# def timer(number_of_secs):
#     while number_of_secs:
#         m, s = divmod(number_of_secs, 60)
#         min_sec_format = '{:02d}:{:02d}'.format(m, s)
#         ctypes.windll.kernel32.SetConsoleTitleW(f"Password Manager 🔐 | Access Granted ✔ | {min_sec_format}")
        
#     main()


def choice_option():
    number = input("\n\n\nChoice option: ")
    try:
        if number == '1':
            if platform == "win32":
                os.system("cls")
            else:
                os.system("clear")

            print("Password Manager | By Morozov")
            print("[1] none\n\n[2] none\n\n[3] Back to menu")
            google()
            
        
        elif number == '2':
            if platform == "win32":
                os.system("cls")
            else:
                os.system("clear")

            print("Password Manager | By Morozov")
            print("[1] none | none\n\n[2] Back to menu")
            vkontakte()

        elif number == '3':
            if platform == "win32":
                os.system("cls")
            else:
                os.system("clear")

            print("Password Manager | By Morozov")
            print("[1] none | none\n\n[2] Back to menu")
            github()
            
        elif number == '4':
            if platform == 'win32':
                os.system('cls')
            else:
                os.system('clear')
            
            print("Password Manager | By Morozov")
            print("[1] none\n\n[2] none\n\n[3] Back to menu")
            instagram()

        elif number == '5':
            if platform == 'win32':
                os.system('cls')
            else:
                os.system('clear')

            print("Password Manager | By Morozov")
            print("[1] Without symbols (with letters)\n\n[1] Without symbols (with out letters)\n\n[3] With symbols (with letters)\n\n[4] With symbols (without letters)\n\n[5] With letters (with symbols)\n\n[6] With letters (without symbols\\n\n[7] All of this")
            generator()


        elif number == '6':
            os.system("cls")
            os.system("exit")


        else:
            os.system("exit")

    except Exception as ex:
        print(ex)

def google():
    google = input("\n\nChoice number: ")
    if google == '1':
        if platform == "win32":
            os.system("cls")
        else:
            os.system("clear")

        print("Password Manager | By Morozov")
        print("[Email] none\n[Password] none")
        time.sleep(30)
        main()

    elif google == '2':
        if platform == "win32":
            os.system("cls")
        else:
            os.system("clear")

        print("Password Manager | By Morozov")
        print("[Email] none\n[Password] none")
        time.sleep(30)
        main()

    elif google == '3':
        if platform == "win32":
            os.system("cls")
        else:
            os.system("clear")
        main()

    else:
        pass

        option = input(Fore.GREEN + "\n\nExit? | yes/no: ")

        if option == 'yes':
            if platform == "win32":
                    os.system("cls")

            else:
                os.system("clear")

        elif option == 'no':
            main()

def vkontakte():
    vk = input("\n\nChoice number: ")
    if vk == '1':
        if platform == "win32":
            os.system("cls")
        else:
            os.system("clear")
        print("Password Manager | By Morozov")
        print("[Phone] none\n[Login] none\n[Password] none")
        time.sleep(30)
        main()

    elif vk == '2':
        main()

def github():
    gh = input("\n\nChoice number: ")
    if gh == "1":
        if platform == "win32":
            os.system("cls")
        else:
            os.system("clear")
        print("Password Manager | By Morozov")
        print("[Email] none\n[Login] none\n[Password] none")
        time.sleep(30)
        main()

    elif gh == '2':
        main()

def instagram():
    insta = input("\n\nChoice number: ")
    if insta == '1':
        if platform == "win32":
            os.system("cls")
        else:
            os.system("clear")
        print("Password Manager | By Morozov")
        print("[Email] none\n[Login] none\n[Password] none")
        time.sleep(30)
        main()

    elif insta == '2':
        if platform == "win32":
            os.system("cls")
        else:
            os.system("clear")
        print("Password Manager | By Morozov")
        print("[Email] None\n[Login] none\n[Password] none")
        time.sleep(30)
        main()
    
    elif insta == '3':
        if platform == 'win32':
            os.system('cls')
        else:
            os.system('clear')
        main()

def generator():
    digits = '0123456789'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz' 
    symbols = '!#$%&*+-=?@^_0123456789' 
    ally = uppercase + lowercase + symbols
    symbolsuppercase = symbols + digits + uppercase
    symbolslowercase = symbols + digits + lowercase
    pwd = input("\n\nChoice number: ")
    if pwd == '1':
        if platform == "win32":
            os.system('cls')
        else:
            os.system('clear')
        print("Password Manager | By Morozov")
        lenght = int(input("Please write how many length: "))

        for i in range(lenght):
            if platform == "win32":
                os.system('cls')
            else:
                os.system('clear')
            password = ''.join(random.sample(lowercase, lenght))
            print("Password Manager | By Morozov")
            print(f"Your Password: {password}")
    
    if pwd == '2':
        if platform == "win32":
            os.system('cls')
        else:
            os.system('clear')
        print("Password Manager | By Morozov")
        lenght = int(input("Please write how many length: "))

        for i in range(lenght):
            if platform == "win32":
                os.system('cls')
            else:
                os.system('clear')
            password = ''.join(random.sample(symbolsuppercase, lenght))
            print("Password Manager | By Morozov")
            print(f"Your Password: {password}")
                
    if pwd == '3':
        if platform == "win32":
            os.system('cls')
        else:
            os.system('clear')
        print("Password Manager | By Morozov")
        lenght = int(input("Please write how many length: "))

        for i in range(lenght):
            if platform == "win32":
                os.system('cls')
            else:
                os.system('clear')
            password = ''.join(random.sample(symbolslowercase, lenght))
            print("Password Manager | By Morozov")
            print(f"Your Password: {password}")
    
    elif pwd == '5':
        if platform == "win32":
            os.system('cls')
        else:
            os.system('clear')
        print("Password Manager | By Morozov")


if __name__ == '__main__':
    main()


        # elif number == '+':
        #     os.system("cls")
        #     global code
        #     print("Password Manager | By Morozov")
        #     password = input("Write Password: ")
        #     if password == code:
        #         if platform == 'win32':
        #             os.system("cls")
        #             print("Password Manger | By Morozov\n\n")
        #             print("[1] Create ")

        #         else:
        #             os.system("clear")
        #             print("Password Manger | By Morozov\n\n")
        #             print("[1] Create ")
                    
        #     manage_passwords()

        # def manage_passwords():
#     number = input("\n\nChoice option: ")
#     try: 
#         if number == '1':
#             print("text")

#         else:
#             os.system("cls")
#             os.system("exit")

#     except Exception as ex:
#         print(ex)
