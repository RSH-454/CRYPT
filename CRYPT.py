import os
import getpass
import hashlib

file_data = 'SavedData.txt'
auth = "SetPassword.txt"

def header():
    os.system("cls" if os.name == "nt" else "clear")
    print(r"""
   ██████╗██████╗ ██╗   ██╗██████╗ ████████╗
  ██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝
  ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   
  ██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   
  ╚██████╗██║  ██║   ██║   ██║        ██║   
   ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝  

               PASSWORD SAVER
                  ver 1.0
""")
    
#This function hides the files. 
def hide_files():
    if not os.path.exists(file_data or auth): 
       return  
    if os.name == 'nt':
        os.system('attrib +h ' + file_data)
    else:
        if not file_data.startswith('.'):
            os.rename(file_data, '.' + file_data)

#This function allows the user to save new data. 
def save():
    print('Enter name of the account: ')
    Account = input()
    Account = Account.strip()
    print('Enter password: ')
    Password = input()
    Password = Password.strip()
    with open(file_data, 'a') as f:
        f.write("Account: " + Account + " " + "Password: " + Password + "\n")
        hide_files()

#This function allows the user to search for previously saved data.
def search():
    print('Enter the name of the account you want to view: ')
    Account = input().strip()         
    if check_file(file_data):
        print("No passwords saved yet.")
        return
    with open(file_data, 'r') as f:
        content = f.read()
        for line in content.splitlines():
            if "Account:" in line and "Password:" in line:
                saved_account = line.split("Account:", 1)[1].split("Password:", 1)[0].strip()
                if saved_account == Account:
                    print(line)
                    break
        else:
            print("Account not found.")

#This function allows the user to view all previously saved data.
def view_all():
    if check_file(file_data):
        print("No passwords saved yet.")
        return
    with open(file_data, 'r') as f:
        content = f.read()
        print(content)          

#This function checks if the file exists or if it is empty.
def check_file(Path):
    return (not os.path.exists(Path)) or os.path.getsize(Path) == 0

#this function hashes the password.
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

#This function allows the user to create and set a password for access. 
def access():
    if check_file(auth):
        set_password = input('Create a password to access the password saver: ')
        hash_password(set_password)
        with open(auth, 'w') as f:
            f.write(hash_password(set_password))
    else:
        with open(auth, 'r') as f:
            set_password = f.read()
    while True:
        password = getpass.getpass('Enter password: ')
        if hash_password(password) == set_password:
            print('[ACCESS GRANTED]\n')
            break
        else:
            print('[ACCESS DENIED]: Incorrect password. Try again.\n')
            hide_files()

header()
access()
input('Press enter to continue...\n')
while True:
    Option = input('Choose option: \n 1. Save \n 2. Search \n 3. View all \n 4. Exit\nOption: ')
 
    if Option == '1':
        save()
        input('Press enter to return to menu...\n')

    elif Option == '2':
        search()
        input('Press enter to return to menu...\n')

    elif Option == '3':
        view_all()
        input('Press enter to return to menu...\n')

    elif Option == '4':
        break 