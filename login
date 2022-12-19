class user:
    name = ''
    email= ''
    password = ''
    login = False
    
    def login(self):
        email = input("Enter email")
        password = input("Enter password")
        
        if email == self.email and password == self.password:
            login = True
            print("login Successful")
        

        else:
            print("login faild.")


    def logout(self):
        login =False
        print("logout")
        
    def isloggedIn(self):
        if self.iogin:
            return True
        else:
            return False
    def profie(self):
        if isloggedIn():
            print(self.name,"\n",self.email)
        else:
            print("user is not logout in")
        
        

user1 = user()

user1.name = "Dihan"
user1.email = "dihank505@gmail.com"
user1.password = "12345"

user1.login()






hello = input()

