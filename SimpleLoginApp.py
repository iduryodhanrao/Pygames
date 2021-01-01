from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager
from database import Database

class CreateAccountWindow(Screen):
    nam = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.nam.text != '' and self.email.text != '' and self.email.text.count('@') == 1 and self.email.text.count('.') > 0:
            if self.password != '':
                rc = db.add_user(self.email.text, self.password.text, self.nam.text)
                if rc == 1:
                    self.reset()
                    sm.current = "login"
                else:
                    popUpForm("Invalid Form", "Email exists already")
                    #invalidForm("User exists already")
            else:
                popUpForm("Invalid Form", "Please fill in all inputs with valid information")
                #invalidForm()
        else:
            popUpForm("Invalid Form", "Please fill in all inputs with valid information")
            #invalidForm()


    def login(self):
        self.reset()
        sm.current="login"

    def reset(self):
        self.email.txt =""
        self.password.text=""
        self.nam.text=""


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        #print("nam" , self.manager.get_screen('create').nam.text)

        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            #invalidLogin()
            popUpForm("Invalid Login", "Please fill in all inputs with valid information.")

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""


class MainWindow(Screen):
    n=ObjectProperty(None)
    created=ObjectProperty(None)
    email=ObjectProperty(None)
    current = ""
    def logOut(self):
        sm.current = "login"

    def on_enter(self, *args):
        password, name, create = db.get_user(self.current)
        self.n.text = "Account Name: " + name
        self.email.text = "Email:" + self.current
        self.created.text = "Created On: " + create



#class WindowManager(ScreenManager):
#    pass

def popUpForm(title,desc):
    pop = Popup(title=title,
                content=Label(text=desc),
                 size_hint=(None,None), size=(400, 200))
    pop.open()

kv = Builder.load_file("login.kv")  # loads the kv file design widgets
#sm = WindowManager()
db = Database("users.txt")
sm = ScreenManager()
sm.add_widget(LoginWindow(name="login"))
sm.add_widget(CreateAccountWindow(name="create"))
sm.add_widget(MainWindow(name="main"))
sm.current = "login"


class SimpleLoginApp(App):
    def build(self):
        return sm

if __name__ == '__main__' :
    SimpleLoginApp().run()



