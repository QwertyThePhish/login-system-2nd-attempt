#Second attempt at login system
#Import neccessary imports
import re
from cryptography.fernet import Fernet
import random
import socket
import keyboard

#Get the user's name and greet them as well as provide options
get_name = input("Enter your name: ")
print("Hello {}, welcome to my login system, what would you like to do?".format(get_name))
print("""\
    1. Create account(working)

    2. Login(working, but hashing still being worked on)

    3. Generate a password(under construction)

    4. additional options(working)
""", end="")

get_option = int(input("Enter option number(e.g 1, 2, 3, 4): "))

#first option for creating a user account
if get_option == 1:

    def check_if_user_exists(usr, users, cross_check):

        with open("users.txt", "r") as existing_users_file:
            for i in existing_users_file.readlines():
                users.append(i)

        with open("checking.txt", "w") as new_user_file:
            new_user_file.write(usr + "\n")
        
        with open("checking.txt", "r") as new_user_file_read:
            for i in new_user_file_read.readlines():
                cross_check.append(i)

        for username in cross_check:
            if username in users:
                print("user already exists")
                return "try another username"
            
            
            else:
                print("username is new")
                with open("users.txt", "a") as added_to_users_database:
                    added_to_users_database.writelines(usr + "\n")
                return "username accepted"


    def password_check(passwd):
        if re.search("[0-9]+", passwd) and re.search("[A-Z]+", passwd) and len(passwd) >= 8:
            print("Password is suitable")
            return "Password valid"
        else:
            print("""\
            PASSWORD GUIDELINES:
        
            1. Passwords must contain suitable length(8 character minimum)

            2. Password must contain numbers(0-9)

            3. (optional)Passwords must contain special characters(#$%!@*?)
            """, end="")
            return "Password validation failed"

    def password_hashed(passwd):
        key = Fernet.generate_key()
        fernet = Fernet(key)
        encrypt_passwd = str(fernet.encrypt(passwd.encode()))
        with open("passwordhashes.txt", "a") as hashfile:
            hashfile.write(encrypt_passwd + "\n")

        return "Password encrypted"

    def account_creation(usr, passwd):
        with open("accountnames.txt", "a") as accounts:
            accounts.write(usr + " " + passwd + "\n")
        return "Account created"
    
    def log_in(usr, passwd, users, cross_check):
        if check_if_user_exists(usr, users, cross_check) == "try another username":
            print("user creation failed")
        else:
            if password_check(passwd) == "Password valid":
                print(password_hashed(passwd))
                print(account_creation(usr, passwd))
            else:
                print("password creation failed")
    
    get_username = input("Enter username(Note: do not use actual name): ")
    print("""\
        PASSWORD GUIDELINES:
        
        1. Passwords must contain suitable length(8 character minimum)

        2. Password must contain numbers(0-9)

        3. Passwords must contain special characters(#$%!@*?)
        """, end="")
    
    get_password = input("Enter password: ")
    
    users_list:list = []
    empty_list:list = []
    
    log_in(get_username, get_password, users_list, empty_list)

#second option for loggin into the account you have made
elif get_option == 2:
    
    print("Enter your user credentials")
    username = input("Enter username: ")
    password = input("Enter password: ")
    user_check_list:list = []
    user_account_check_list:list = []

    def database_check(usr, passw, user_check, account):
        with open("account_check.txt", "w") as account_check:
            account_check.write(usr + " " + passw + "\n")

        with open("account_check.txt", "r") as account_list:
            for a in account_list.readlines():
                user_check.append(a)

        with open("accountnames.txt", "r") as account_cross_check:
            for i in account_cross_check.readlines():
                account.append(i)

        for j in user_check:
            if j in account:
                print("Welcome {}".format(usr))
                return "Successfully logged in"
            else:
                print("login failed")
                print("""\
                    Reasons:
                    1. username could be incorrect

                    2.password you have issued could be incorrect

                    3. user does not exist in the database

                    """, end="")
                return "Login failed"

    def user_verify(usr, passw, user_check, account):
        print(database_check(usr, passw, user_check, account))

    user_verify(username, password, user_check_list, user_account_check_list)


#generate password(still being worked on)
elif get_option == 3:
    print("Still in progress")


#additional option for ping script and keylogger
elif get_option == 4:
    #ping script
    print("""\What would you like to do: 
                1)ping a site
                2)keylogger
                """, end="")
    get_option_num = int(input("Enter option number: "))
    if get_option_num == 1:

        get_site_name = input("Enter the site name(google/facebook...): ")
        get_domain_type =  input("Enter domain type(org/com/co.za...): ")
        ping = socket.gethostbyname("www.{}.{}".format(get_site_name, get_domain_type))
        print("Pinged {} at {}".format(get_site_name, ping))
    elif get_option_num == 2:
        
        print("Keylogger started...")
        print("Press esc key to stop keylogger from running")
        recording_keys = keyboard.record(until="esc")
        with open("keystrokes.txt", "a") as key_store:
            for key in recording_keys:
                key_store.write(str(key) + "\n")
        print("keylogger stopped")
        
    else:
        print("Please enter valid option number")

