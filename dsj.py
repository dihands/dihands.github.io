class user:
    name = ''
    email= ''
    password = ''
    login = False
    
    def login(self):
        email = input("Enter Id")
        password = input("Enter password")
        
        if email == self.email and password == self.password:
            login = False
            print("login Successful")
        

        else:
            print("login faild.")


    def logout(self):
        login =False
        print("logout")
        
    def isloggedIn(self):
        if self.login:
            return True
        else:
            return False
    def profie(self):
        if self.isloggedIn():
            print(self.name,"\n",self.email)
        else:
            print("user is not logout in")
        
        

user1 = user()

user1.name = "THE INFORMATION : https://drive.google.com/drive/folders/13qNZDcyC6ClBSFK5cHbdF8-e6lJ1o0eu?usp=share_link"
user1.email = "DS44DS"
user1.password = "18dihan19"

user1.login()



user1.profie()


hello = input()