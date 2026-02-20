FileName = 'SavedData.txt'
#This function allows the user to save new data. 
def SaveData():
    print('Enter name of the account: ')
    Account = input()
    print('Enter password: ')
    Password = input()
    with open(FileName, 'a') as f:
        f.write("Account: " + Account + " " + "Password: " + Password + "\n")

#This function allows the user to view previously saved data. 
def ViewData():
    print('Enter the name of the account you want to view: ')
    Account = input()
    with open(FileName, 'r') as f:
        content = f.read()
        for line in content.splitlines():  
         if Account in line:
            print(line)    
            break
        else:
          print("Account not found.")

print('[PASSWORD SAVER]')
input('Press enter to continue...\n')
while True:
    Option = input('Choose option: \n 1. Save new password \n 2. View saved passwords \n 3. Exit\nOption: ')

    if Option == '1':
        SaveData()
    elif Option == '2':
        ViewData()
    elif Option == '3':
        break