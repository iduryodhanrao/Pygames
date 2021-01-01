import kivy
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.button import Button
import random
from kivy import Config
Config.set('graphics', 'multisamples', '0')

#Global Variables
#gameList=list(range(6))
#uList=["","","","","",""]
#prevID=10

#Login Screen and its methods
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        bx = BoxLayout(orientation='vertical')
        NumButton = Button(font_size=50, text="Number Puzzle");bx.add_widget(NumButton)
        AlphButton = Button(font_size=50,text="Alphabet Puzzle");bx.add_widget(AlphButton)
        CartoonButton = Button(font_size=50, text='Cartoon Puzzle');bx.add_widget(CartoonButton)
        AnimalButton = Button(font_size=50, text="Animal Puzzle");bx.add_widget(AnimalButton)
        NumButton.bind(on_press=self.changer);AlphButton.bind(on_press=self.changer);
        CartoonButton.bind(on_press=self.changer);AnimalButton.bind(on_press=self.changer);
        self.add_widget(bx)

    def changer(self, *args):
        self.manager.current = "mainscreen"

'''class MyPopup(Popup):
    def show_popup(self):
        b = BoxLayout(orientation='vertical')
        b.add_widget(Label(text="You Won!!", font_size=50, size_hint=(.5, .3)))
        b.add_widget(Button(text="Play Again?", font_size=50, size_hint=(.5, .3), on_press=self.switchscreen))
        b.add_widget(Button(text="Close", font_size=50, size_hint=(.5, .3), on_press=self.switchscreen))
        mypopup = Popup(content=b,title="YaY!!!", auto_dismiss=False,size_hint=(.5,.5))
        
        self.add_widget(b)
'''
#Main Screen and its methods
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_layout = BoxLayout(orientation="vertical")
        #image names/filenames
        NumberImageList = []
        AlphaImageList = []
        CartoonImageList = []
        AnimalImageList = ["aligator.JPG","bear.JPG","dog.JPG","fox.JPG","hippo.JPG","kangaroo.JPG","lion.JPG","monkey.JPG","squirrel.JPG","tiger.JPG","zebra.JPG"]
        #create button labels
        imgList = ["0", "1", "2","3", "4", "5", "6", "7", "8", "9"]
        random.shuffle(imgList)
        #global gameList
        self.prevID=10
        self.uList = ["", "", "", "", "", ""]
        self.gameList = imgList[:3] + imgList[:3]
        random.shuffle(self.gameList)
        self.button = []
        #create buttons with boxlayout for each row
        h_layout = BoxLayout()
        for row in range(6):
            self.button.append(Button(id="id" + str(row),font_size='50',disabled=False,on_press=self.on_button_press))
            h_layout.add_widget(self.button[row])
            #add on press event function
            #self.button[row].bind(on_press=self.on_button_press)


            if row % 2 != 0:
                #add each row layout to mainlayout
                main_layout.add_widget(h_layout)
                h_layout = BoxLayout()
        self.add_widget(main_layout)


    def on_button_press(self, instance):
        currID = int(instance.id[-1])
        if instance.text=="":
            print(instance.background_normal)
            instance.background_normal='images/'+self.gameList[currID]
            instance.text=self.gameList[currID] #show text
            self.uList[int(currID)]=instance.text #save pressed text to UserList
            if self.prevID != 10: #not a first time press
                if self.button[self.prevID].text == instance.text: #prev and current pressed buttons have same values
                    pass
                else: #if no match flip the prev button
                    if self.uList.count(self.button[self.prevID].text) < 2:
                        self.button[self.prevID].text = ""
                        self.uList[self.prevID]=""
            self.prevID=currID
        else:
            print(instance.background_normal)
            if self.uList.count(instance.text) < 2:
                instance.text=""

        if self.uList.count('') == 0:
            print(self.uList.count(''))
            for row in range(6):
                self.button[row].disabled=True

            b = FloatLayout()
            b.add_widget(Label(text="You Won!!", font_size=30, pos_hint={'x':0.4,'y':.7},size_hint=(.25, .2)))
            b.add_widget(Button(text="Play Again?", font_size=30,pos_hint={'x':0.4,'y':.5},size_hint=(.25, .2), on_press=self.switchscreen))
            b.add_widget(Button(text="Close", font_size=30,pos_hint={'x':0.4,'y':.3},size_hint=(.25, .2), on_press=self.switchscreen))
            self.add_widget(b)

    def switchscreen(self,instance):
        if instance.text == 'Close':
            App.get_running_app().stop()
        else:
            for row in range(6):
                self.button[row].text=""
            self.__init__()
            self.manager.current = 'loginscreen'




class PicMatchGame(App):

    def build(self):

        # create screen manager
        sm = ScreenManager()
        sc_login = LoginScreen(name="loginscreen")
        sc_main = MainScreen(name="mainscreen")
        sm.add_widget(sc_login)
        sm.add_widget(sc_main)
        print(sm.current_screen)

        return sm


if __name__ == '__main__':
    PicMatchGame().run()
