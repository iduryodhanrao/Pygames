import datetime


class Database:
    #initialize Database class
    def __init__(self,filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    #read all login details from file
    def load(self):
        self.file = open(self.filename, "r")
        self.users = {}

        for line in self.file:
            email, password, name, created = line.strip().split(";")
            self.users[email] = (password,name,created)

        self.file.close()

    #get the login details for email passed
    def get_user(self,email):
        if email in self.users:
            return self.users[email]
        else:
            return -1

    #validate user if they already exist in credential file
    def validate(self,email, password):
        if self.get_user(email) != -1:
            return self.users[email][0] == password
        else:
            return False

    #add user with parameter passed
    def add_user(self,email, password, name):
        if email.strip() not in self.users:
            self.users[email.strip()] = (password.strip(), name.strip(), Database.get_date())
            self.save()
            return 1
        else:
            print("Email exists already")
            return -1

    #save the user details to credential file
    def save(self):
        with open(self.filename,"w") as f:
            for user in self.users:
                f.write(user+";"+self.users[user][0]+";"+self.users[user][1]+";"+self.users[user][2]+"\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]

