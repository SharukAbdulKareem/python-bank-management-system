from datetime import datetime
now = datetime.now()

#function to register users
def usrrgstr():
  while True:
      print("************** USER REGISTER **************")
      print("Please provide the following details")
      firstName = input("Enter your first name:")                                   #function to get user details
      lastName = input("Enter your last name:")
      ph = input("Enter your phone number in 10 digits:")
      ph = str(ph)
      paid_amount = 500
      idNum = input("Please enter your passport number:")
      accountype = input('Enter your preferred type of account, enter "S" savings or "C" for current:')
      while True:
          if accountype == "S" or accountype == "C":
              break
          else:
              accountype = input('invalid Enter, Please enter your preferred type of account, enter "S" savings or "C" for current:')

      with open("id.txt", "r") as file:
          k = file.read()
      userid = int(k)                                                                                                  #function to assignuser id
      userid = userid + 1                                                                                              #reads id file and adds 1 for new user
      userid = str(userid)
      print("REGISTRATION SUCCESSFUL, Your account number is:", userid)
      userpass = idNum + accountype
      print('your password is', userpass)
      with open("id.txt", "w") as file:
          z = file.write(userid)                                                                                       #function to rewrite id

      user = open("user.txt", "a")                                                                                     #function to append user details to file
      user.write(firstName + ":" + lastName + ":" + idNum + ":" + accountype + ":" + userid + ":" + userpass + ":" + ph + ":" +str(paid_amount) +"\n")
      user.close()


#function to register  staffs
def staffreg():
    print("************** STAFF REGISTER **************")
    print("Please provide the following details")
    usrname = input("Please enter a username for staff:")                                #function to enter staff pasword and id
    usrpassword = input("Please enter a password for staff:")

    with open("staff.txt", "r") as file:
        for recline in file:                                                             #function to check if staff id exists
            reclist = recline.strip().split(":")
            if reclist[0] == usrname:
                print('Username already exist, please try again')
                break
            else:
                with open("staff.txt", "a") as file:
                    file.write(usrname + ":" + usrpassword + "\n")
                    print('Registration successful!')
                    break

#function to go back to main menu
def sprback():
    ans1 = input('Enter "Q" to quit:')                            #asks for user input
    while True:
        if ans1 == 'Q':                                           #calls menu page
            menu()
        else:
            print('invalid input please try again')
            ans1 = input('Enter "Q" to quit')

#function for super user
def superuser():
    print('**************SUPERUSER LOGIN**************')
    while True:
        supername = input('Enter your superuser ID:')                                  #function to get superuser id and password
        if supername == 'AS234001':
            superpss = input('Enter your super user password:')
            if superpss == '123456':                                                   #displays choices
                print('Welcome Abdullah')
                print('[1] Register new staff')
                print('[2] Display all users')
                print('[3] Return to Main Menu')
                print()
                superChoice = input("Enter your option:")
                if superChoice == '1':                                                 #function to call user choice
                    staffreg()
                elif superChoice == '2':
                    dispusr()
                elif superChoice == '3':
                    menu()
                else:
                    print("invalid option")
                    superChoice = input("Enter your option:")
            else:
                print('Invalid password')
                superpss = input('Enter your super user password:')
        else:
            print('Incorrect super user name, please try again')
            supername = input('Enter your superuser ID :')


#function for staffs to login
def stafflogin():
    print("**************STAFF LOGIN**************")
    stf_id = input("Please enter your user ID: ")                                        #function to enter staff id
    stf_pss = input("Please enter your password: ")                                      #function to enter staff  password
    with open("staff.txt", "r") as file:
        foundrecd = "notfound"
        for recline in file:
            reclist = recline.strip().split(":")
            if reclist[0] == stf_id and reclist[1] == stf_pss:                           #function to check if login credentials are right
                foundrecd = reclist
                break
        if foundrecd == "notfound":
            print("invalid credentials, please try again")
        else:
            print("Login Successful..."'\n')
            staff()
    return foundrecd

#function for users to login
def usrlogn():
    print("**************USER LOGIN**************")
    usr_id = input("Please enter your user ID: ")                                        #function to enter user id
    usr_pss = input("Please enter your password: ")                                      #function to enter user password
    with open("user.txt", "r") as file:
        foundrec = "notfound"
        for recline in file:                                                              #function to check if login credentials are right
            reclist = recline.strip().split(":")
            if reclist[4] == usr_id and reclist[5] == usr_pss:
                foundrec = reclist
                break
        if foundrec == "notfound":
            print('\n'"Invalid credentials please try again!!!")

        else:
            print("Login Successful...\n")
            user(foundrec)
            return reclist
    return foundrec

#function to display user records
def dispusr():
    with open("user.txt", "r") as fh:                               #opens and reads file
        print("=" * 123)                                            #function to format
        print("|" +"First name".center(20) + "|" + "last name".center(20) + "|" + "Passport".center(
            10) + "|" + "Account Type".center(10) + "|" +"Userid".center(10)+ "|" +"USR Password".center(10)+ "|" +"Phone No".center(10) + "|" +"Current Balance ($)".center(20) + "|")
        print("=" * 123)
        for rec in fh:
            rlst = rec.strip().split(":")
            print("|" +rlst[0].center(20).ljust(20) + "|" + rlst[1].center(20).ljust(20) + "|" + rlst[2].ljust(10) + "|" + rlst[3].center(12) +
                  "|" + rlst[4].ljust(10) + "|" + rlst[5].ljust(12)+ "|" + rlst[6].ljust(10) + "|"+ rlst[7].center(20).ljust(10)  + "|")
        print("=" * 123)
    print("\n\n")
    print('success')
    sprback()

#function to get index of file
def get_index(file_name):
    ac_num=input("Enter user id: ")                                                          #gets users id

    file=open(file_name,'r')                                                                 #opens user file and read the id
    file_list=[]
    for x in file:
        file_list.append(x.split(":"))
    for i in file_list:                                                                      #checks id number
        if i[4] == ac_num:                                                                   #function to search for id
            return (file_list.index(i))                                                      #returns index
    else:
        print('Invalid ID number, please try again')
        ac_num = input("Enter user id: ")


#function to change customer details
#function to change customer contact number
def change_cont(file_name):
    ind = get_index(file_name)
    new_cont=input("Please enter new contact: ")                                             #asks input for new contact number
    file=open(file_name,'r')                                                                 #function to open and read user file,read
    file_list = []
    for x in file:
        file_list.append(x.split(":"))

    record=file_list[ind]

    record[6]=new_cont

    file.close()
    #formatting the file
    file=open(file_name,'w')
    file.write("")
    file.close()

    file=open(file_name,'a')                                                                  #function to add the new contact number to the file
    print('contact changed successfully')

    for rec in file_list:
        for i in rec:
            file.write(i)
            if rec.index(i) != len(rec)-1:
                file.write(":")


#function to change customer details
#function to change customer passport number
def changePssprtno(file_name):
    ind = get_index(file_name)
    new_pssprt = input("Please enter new passport number: ")                       #asks input for new passport number
    file = open(file_name, 'r')                                                    #function to open file,read and splits it
    file_list = []
    for x in file:
        file_list.append(x.split(":"))

    record = file_list[ind]

    record[2] = new_pssprt

    file.close()
    # formatting the file
    file = open(file_name, 'w')
    file.write("")
    file.close()

    file = open(file_name, 'a')                                                    #function to add the new passport number to the file
    print('Passport no changed successfully')

    for rec in file_list:
        for i in rec:
            file.write(i)
            if rec.index(i) != len(rec) - 1:
                file.write(":")


#function for staffs
#function to create user account
#function to edit customer account
#function to print customer statements
def staff():
    while True:
        print("[1}Create user account")
        print("[2]View customer details")
        print("[3]Change customer phone  number")
        print("[4]Change customer passport number")
        print('[5]Customer statement')
        print('[6]Exit''\n')
        stfchoice = input("Enter your option:")                                         #asks for users choice
        if stfchoice == '1':                                                            #from here calls functions according to staff choice
            print("User register")
            usrrgstr()
        elif stfchoice == '2':
            print("customer details")
            dispusr()
        elif stfchoice == '3':
            print("change phone number")
            change_cont("user.txt")
        elif stfchoice == '4':
            print("change passport number")
            changePssprtno("user.txt")
        elif stfchoice == '5':
            print("Print customer statement")
            stfstatement()
        elif stfchoice == '6':
            menu()
        else:
            print("invalid option")
            stfchoice = input("Enter your option:")


#function for users
#function to make deposit
#function to change user password
def user(foundrec):
    while True:
        print('Welcome'+ "\t" + foundrec[0])                                            #Welcome message
        print("[1}Make Deposit")                                                        #Displays choices
        print("[2]Make Withdrawal")
        print("[3}Change password")
        print('[4]Print statement')
        print("[5}Exit program \n")
        usrwish = input("Enter your option:")                                            #Ask for user input
        if usrwish == '1':                                                               #from here calls functions passed with parameters according user choice
            print('Make deposit')
            deposit(foundrec)
            break
        elif usrwish == '2':
            print('withdraw')
            withdraw(foundrec)
            break
        elif usrwish == '3':
            print('change password')
            chngpas(foundrec)
        elif usrwish == '4':
            print('my statement')
            usrstatement(foundrec)
        elif usrwish == '5':
            menu()
        else:
            print("invalid option")

#function to deposit money
def deposit(foundrec):
    while True:
        foundrec[4] = str(foundrec[4])                                                               #converts to string
        foundrec[7] = int(foundrec[7])                                                               #converts to integer
        amountin = int(input('Enter the amount you want to deposit,$:'))
        balance = amountin + foundrec[7]
        amountin1 = str(amountin)
        bal = str(balance)

        with open("statement.txt", "a") as file:                                                     #fuction to open statement file and write new balance with all necessary details
            file.write(str(datetime.date(datetime.now())) + ":" + foundrec[4] + ":" + 'deposit' + ":" + amountin1 + ":" + bal + "\n")

        allrec = []
        with open("user.txt", "r") as fh:                                                  #function to read current user balance
            for rec in fh:
                reclist = rec.strip().split(":")
                allrec.append(reclist)
        bal = bal
        ind = -1
        nor = len(allrec)
        for cnt in range(0, nor):                                                          #function to check deposit amount
            if foundrec[4] == allrec[cnt][4]:
                ind = cnt
                print('deposit successful!')
                break

        allrec[ind][7] = bal                                                                #Function to write new balance in user file
        with open("user.txt", "w") as fh:
            nor = len(allrec)
            for cnt in range(0, nor):
                rec = ":".join(allrec[cnt]) + "\n"
                fh.write(rec)
        break


#function to withdraw money
def withdraw(foundrec):
    while True:
        foundrec[7] = int(foundrec[7])

        if foundrec[3] == 'S':                                                                     #function to check is account type is savings
            print('savings account')
            if foundrec[7] >= 100:                                                                 #asks to enter withdrawal money if balance is greater than 100
                amountout = int(input('Enter the amount you want to withdraw,$:'))
                if foundrec[7] > amountout:
                    balance = int(foundrec[7]) - int(amountout)
                    with open("statement.txt", "a") as file:                                       #adds new withdrawal money new balance all details into file
                        file.write(str(datetime.date(datetime.now())) + ":" + foundrec[4] + ":" + 'withdraw' + ":" + str(amountout) + ":" + str(balance) +  "\n")

                        allrec = []
                        with open("user.txt", "r") as fh:
                            for rec in fh:
                                reclist = rec.strip().split(":")
                                allrec.append(reclist)
                        balance = balance
                        ind = -1
                        nor = len(allrec)
                        for cnt in range(0, nor):
                            if foundrec[4] == allrec[cnt][4]:
                                ind = cnt
                                print('Withdrawal successful!')
                                break

                        allrec[ind][7] = str(balance)
                        with open("user.txt", "w") as fh:
                            nor = len(allrec)
                            for cnt in range(0, nor):
                                rec = ":".join(allrec[cnt]) + "\n"
                                fh.write(rec)
                else:
                    print("insuffient balance, withdraw amount is greater than account balance")
                    sprback()
                    break
            else:
                print('Insufficient balance,minimum balance of $ 100 is required ')
                sprback()
                break
        elif foundrec[3] == 'C':                                                                              #function to check is account type is Current
            print('Current account')
            amountout2 = int(input('enter the amount you want to withdraw,$:'))
            if foundrec[7] >= 500:                                                                            #asks for withdraw money if balance is more than 500
                balance2 = foundrec[7] - int(amountout2)
                with open("statement.txt", "a") as file:                                                      #adds new withdrawal money new balance all details into file
                    file.write(str(datetime.date(datetime.now())) + ":" + foundrec[4] + ":" + 'withdraw' + ":" + str(amountout2) + ":" + str(balance2))

                    allrec = []
                    with open("user.txt", "r") as fh:
                        for rec in fh:
                            reclist = rec.strip().split(":")
                            allrec.append(reclist)
                    balance2 = balance2
                    ind = -1
                    nor = len(allrec)
                    for cnt in range(0, nor):
                        if foundrec[4] == allrec[cnt][4]:
                            ind = cnt
                            print('Withdrawal successful!')
                            break

                    allrec[ind][7] = str(balance2)
                    with open("user.txt", "w") as fh:
                        nor = len(allrec)
                        for cnt in range(0, nor):
                            rec = ":".join(allrec[cnt]) + "\n"
                            fh.write(rec)

            else:
                print('Insufficient balance,minimum balance of RM 500 is required ')                    #displays message if balance is lesser than 500
                sprback()
                break
        else:
            print('not found')                                                                          #displays if balance is not found
            sprback()
            break

#function to change user password
def chngpas(foundrec):
    allrec = []
    with open("user.txt", "r") as fh:                                                      #opens and reads file
        for rec in fh:
            reclist = rec.strip().split(":")
            allrec.append(reclist)
    newpass = input("Please Enter new Password : ")                                        #asks for new password
    ind = -1
    nor = len(allrec)
    for cnt in range(0, nor):
        if foundrec[5] == allrec[cnt][5]:                                                  #changes new password
            ind = cnt
            print('Password changed successfully\n')
            break

    allrec[ind][5] = newpass
    with open("user.txt", "w") as fh:                                                      #Writes the new password in file
        nor = len(allrec)
        for cnt in range(0, nor):
            rec = ":".join(allrec[cnt]) + "\n"
            fh.write(rec)


#function to print user statment by user
def usrstatement(foundrec):
    allrec = []
    startdate =str(input('Enter the start date(yyyy-mm-dd) :'))                                            #get start date
    enddate = str(input('Enter the end date(yyyy-mm-dd) :'))                                               #get end date

    with open("statement.txt", "r") as fh:                                                                 #opens and reads file
        for line in fh:
            allrec.append(line.strip().split(":"))
    print("=" * 81)                                                                                        #function to format
    print("|" + "Date".center(15) + "|" + "User Id".center(14) + "|" + "Transaction Type".center(15)
          + "|" + "Amount".center(15) +"|" + "Balance ($)".center(15) + "|")
    print("=" * 81)
    for cnt in range(0, len(allrec)):                                                                       #function to print details if condition matches
        if (foundrec[4] == allrec[cnt][1]) and allrec[cnt][0] >= startdate and allrec[cnt][0] <= enddate:
            print( "|" + allrec[cnt][0].ljust(15) + "|" + allrec[cnt][1].center(14) + "|" + allrec[cnt][2].rjust(16)
                   + "|" + allrec[cnt][3].rjust(15) + "|" + allrec[cnt][4].rjust(15) + "|")
    print("=" * 81)

#function to print transaction statement by staff
def stfstatement():
    userid = input('Enter the user id you wish to find:')                                                #get user id
    startdate = str(input('Enter the start date(yyyy-mm-dd):'))                                          #get start date
    enddate = str(input('Enter the end date(yyyy-mm-dd):'))                                              #get end date
    allrec = []
    with open("statement.txt", "r") as fh:                                                               #opens and reads file
        for line in fh:
            allrec.append(line.strip().split(":"))
    print("=" * 81)                                                                                      #function to format file
    print("|" + "Date".center(15) + "|" + "User Id".center(14) + "|" + "Transaction Type".center(15)
          + "|" + "Amount $".center(15) + "|" + "Balance ($)".center(15) + "|")
    print("=" * 81)
    for cnt in range(0, len(allrec)):
        if (userid == allrec[cnt][1]) and allrec[cnt][0] >= startdate and allrec[cnt][0] <= enddate:     #function to print details if condition matches
            print("|" + allrec[cnt][0].ljust(15) + "|" + allrec[cnt][1].center(14) + "|" + allrec[cnt][2].rjust(15)
                  + "|" + allrec[cnt][3].rjust(15) + "|" + allrec[cnt][4].rjust(16) + "|")
    print("=" * 81)


#main logic
def menu():
    print("MAIN MENU")
    print("Welcome to XYZ Bank \n Enter '1' if you are an user, Enter '2' if you are an admin , Enter '3' if you are a super user")    #displays user options
    print("[1}Login User")
    print("[2]Login Admin")
    print("[3]Login Super User")
    print()
    while True:
        userChoice = input("Enter your option:")                                              #Asks for user input
        if userChoice == '1':                                                                 #from here calls functions according user choice
            x = usrlogn()
        elif userChoice == '2':
            stafflogin()
        elif userChoice == '3':
            superuser()
        else:
            print("Invalid option please try again")
menu()