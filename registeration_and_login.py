import re
class registration:
    # creating  a function for registration
    def register(self):
        name = input("Enter username: ")

        # declaring the required variables
        symbol = "0123456789!@#$%^&*"
        pattern = r"@."
        x = re.findall(pattern, name)

        # checking starting character
        if name[0] in symbol:
            print("Starting character should not be numbers or special charater")
            REG.register()

        # checking does username have '@'
        elif '@'  not in name:
            print("Username should contain '@'  followed by '.' ")
            REG.register()

        # checking does username have '.'
        elif '.' not in name:
            print("Username should contain '.' after '@' ")
            REG.register()

        # checking '.' is immediate next to '@'
        elif "@." in x:
         print("'.' should not ne immediate next to '@'")
         REG.register()

        # calling the password function
        else:
            REG.pass_word(name)


    # creating  function for password
    def pass_word(self,name):
        name=name
        password = input("Enter password: ")

        # declaring the required variables
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        ALPHABETS = alphabets.upper()
        numbers = "0123456789"
        charcters="!@#$%&*_"
        var1 = var2 = var3 = var4 = 0

        # checking the length of the password
        if len(password) >= 5 and len(password) < 16:
            # for loop to check the conditions
            for i in password:

                # checking password has number,if so incrementing the variable
                if i in numbers:
                    var1 += 1

                # checking password has lowercase letter,if so incrementing the variable
                if i in alphabets:
                    var2 += 1

                # checking password has upercase letter,if so incrementing the variable
                if i in ALPHABETS:
                    var3 += 1

                # checking password has specail characters,if so incrementing the variable
                if i in charcters:
                    var4 += 1

            # calling a function to validate the password
            REG.validating_password(var1, var2, var3,var4,name,password)

        else:
            print("Password length should be greater than 5 and lesser than 16")
            REG.pass_word(name)


    # creating a function to validate the password entered
    def validating_password(self,var1, var2, var3,var4,name,password):
        # if all variable is greater than 0, it satisfies the condition
        if var1 > 0 and var2 > 0 and var3 > 0 and var4 > 0:

            # checking password and confirm password
            confirm_password=input("Confirm password: ")
            if password == confirm_password:
             print("SUCCESSFULLY REGISTERED")
             REG.storing_data(name, password)
            else:
                print("Password and confirm password are not same")
                print("Create password again")
                REG.pass_word(name)

        elif var1 == 0:
            print("Password should contain a number")
            REG.pass_word(name)

        elif var2 == 0:
            print("Password should contain a lowercase")
            REG.pass_word(name)

        elif var3 == 0:
            print("Password should conatin a uppercase")
            REG.pass_word(name)


        elif var4 ==  0:
            print("Pssword should contain a special character")
            REG.pass_word(name)


    # creating a fucntion to store the users name and password
    def storing_data(self,name,password):
        store=open("assignment_0_txt.txt","a")
        store.write(name+","+password+"\n")
        store.close()
        REG.login()


    # creating a function to login
    def login(self):
        #fetching the data of the users which is stored in a text file
        dictionary = {}
        file = open("assignment_0_txt.txt", "r")
        for i in file:
            name, password = i.split(",")
            password = password.strip()
            dictionary[name] = password
        print("       LOGIN       ")
        login_name = input("Enter username:  ")
        login_password = input("Enter password: ")

        # checking username is in the database
        if login_name not in dictionary:
            print("Username not found")
            print("     REGISTER    ")
            REG.register()

        # checking login_name and password matches the database
        for i, j in dictionary.items():
            if login_name == i and login_password == j:
                print("         LOGIN SUCCESSFULL          ")

            elif login_name == i and login_password != j:
                print("Password is worng")
                print()

                # creating a function to select login again or forget password
                def log_or_pass():
                    log_or_forgetpass = input("1.Login again\n2.Forget password\nChoose 1 or 2: ")
                    if str(log_or_forgetpass) == "1":
                        REG.login()
                    elif str(log_or_forgetpass) == "2":
                        REG.forget_password(dictionary)
                    else:
                        print("Choose wisely\n")
                        log_or_pass()

                # calling the created function log_or_pass()
                log_or_pass()


    # creating a function forget_password
    def forget_password(self,dictionary):
        username = input("Enter the registerd username: ")
        if username in dictionary:
            print("Your password is: ", dictionary[username])
            REG.login()
        else:
            print("Username not found,register again")
            REG.register()


# creating a function register_or_login()
def register_or_login():
    reg_or_log = input("1.Register\n2.Login\nSelect 1 or 2: ")
    if str(reg_or_log) == "1":
        print("         REGISTRATION       ")
        REG.register()

    elif str(reg_or_log) == "2":
        print("          LOGIN             ")
        REG.login()
    else:
        print("Choose wisely")
        print()
        register_or_login()


#runs form here
print("                  REGISTRATION AND LOGIN                 ")
# creating an object for the cass registration
REG = registration()
#calling the created function register_or_login
register_or_login()
