import os
import getpass
import hashlib

def header():
    os.system("cls" if os.name == "nt" else "clear")
    print(r"""
   ██████╗██████╗ ██╗   ██╗██████╗ ████████╗
  ██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝
  ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   
  ██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   
  ╚██████╗██║  ██║   ██║   ██║        ██║   
   ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝  

               PASSWORD MANAGER
               ver 0.3.1-beta.2
""")

 #This function names the files depending on the operating system. If the user is on Linux/macOS it hides th by default.   
def file_names():
    if os.name == "nt":  
        return "SavedData.txt", "SetPassword.txt"
    else: 
        return ".SavedData.txt", ".SetPassword.txt"

file_data, auth = file_names()

#This function hides the files. 
def hide_file(filename):
    if os.name == 'nt':
        if os.path.exists(filename):
            os.system(f'attrib +h "{filename}"')

def unhide_file(filename):
    if os.name == 'nt':
        if os.path.exists(filename):
            os.system(f'attrib -h "{filename}"')

#This function allows the user to create and set a password for access. 
def access():
    if check_file(auth):
        set_password = input('Create a password: ').strip()
        stored_hash = hash_password(set_password)
        with open(auth, 'w') as f:
            f.write(stored_hash)
        hide_file(auth)     
    else:
        with open(auth, 'r') as f:
            stored_hash = f.read().strip()
    while True:
        password = getpass.getpass('Enter password: ').strip()
        if hash_password(password) == stored_hash:
            print('[ACCESS GRANTED]\n')
            break
        else:
            print('[ACCESS DENIED]: Incorrect password. Try again.\n')

#This function checks if the file exists or if it is empty.
def check_file(Path):
    return (not os.path.exists(Path)) or os.path.getsize(Path) == 0

#This function hashes the password.
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

#This function allows the user to save new data. 
def save():
    print('Enter name of the account: ')
    Account = input().strip()
    Password = getpass.getpass('Enter password: ').strip()
    unhide_file(file_data)
    with open(file_data, 'a') as f:
        f.write("Account: " + Account + " " + "Password: " + Password + "\n")
    hide_file(file_data)

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

#This function allows the user to reset their password.
def reset_password():
    current_password = getpass.getpass('Enter your current password: ').strip()
    if hash_password(current_password) != open(auth, 'r').read().strip():
        print("Incorrect current password.")
        return
    new_password = getpass.getpass('Enter new password: ').strip()
    confirm_password = getpass.getpass('Confirm new password: ').strip()
    if new_password != confirm_password:
        print("Passwords do not match.")
        return
    unhide_file(auth)
    with open(auth, 'w') as f:
        f.write(hash_password(new_password))
    hide_file(auth)
    print("Password reset successful.")

header()
access()
input('Press enter to continue...\n')
while True:
    Option = input('Choose option: \n 1. Save \n 2. Search \n 3. View all \n 4. Reset Password \n 5. Exit \nOption: ')
 
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
        reset_password()
        input('Press enter to return to menu...\n')

    elif Option == '5':
        os.system("cls" if os.name == "nt" else "clear")
        break 