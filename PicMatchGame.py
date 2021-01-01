import kivy
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.graphics.vertex_instructions import Ellipse, Line
from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty, BooleanProperty, Clock
from kivy.uix.behaviors import DragBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget

kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.button import Button
import random
from kivy import Config

Config.set('graphics', 'multisamples', '0')

# Option Screen and its methods
class Optionscreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bpressed=''
        bx = GridLayout(cols=2)
        NumButton = Button(font_size=50, text="Number Puzzle", on_press=self.changer);
        bx.add_widget(NumButton)
        FamilyButton = Button(font_size=50, text="Family Puzzle",on_press=self.changer);
        bx.add_widget(FamilyButton)
        CartoonButton = Button(font_size=50, text='Cartoon Puzzle',on_press=self.changer);
        bx.add_widget(CartoonButton)
        AnimalButton = Button(font_size=50, text="Animal Puzzle",on_press=self.changer);
        bx.add_widget(AnimalButton)
        PaintButton = Button(font_size=50, text="Paint", on_press=self.changer);
        bx.add_widget(PaintButton)
        ImageShuffleButton = Button(font_size=50, text="Image shuffle", on_press=self.changer);
        bx.add_widget(ImageShuffleButton)
        CloseButton = Button(font_size=50, text="Close", on_press=self.changer);
        bx.add_widget(CloseButton)

        self.add_widget(bx)

    def changer(self,instance, *args):
        self.bpressed=instance.text
        if self.bpressed == 'Paint':
            self.manager.current = "paint"
        elif self.bpressed == 'Image shuffle':
            self.manager.current = "imgshuffle"
        elif self.bpressed == 'Close':
            App.get_running_app().stop()
        else:
            self.manager.current = "mainscreen"


##drag image app start
kv = '''
<ImageWidget>:
    drag_rectangle: self.x, self.y, self.width, self.height
    drag_timeout: 10000000
    drag_distance: 0
    # id - for canvas is set always at higher level and traced by get_group()
    #size: 200, 200
    Widget:
        id: w_canvas
        canvas:
            Color:
                group: 'a'
                rgba: 1,1,1,1
            Rectangle:
                group: 'b'
                pos: root.pos
                size: root.size
                
                source: 'icon.png'
'''

Builder.load_string(kv)


class ImageWidget(DragBehavior, Widget):
    imgicon = StringProperty()
    imgalpha = NumericProperty(1)
    setDrag = BooleanProperty(True)
    def addImage(self):
        rect = self.ids.w_canvas.canvas.get_group('b')[0]
        rect.source = self.imgicon
        clr=self.ids.w_canvas.canvas.get_group('a')[0]
        clr.rgba = [1,1,1,self.imgalpha]

    def on_touch_move(self, touch):
        if self.setDrag and touch.grab_current is self:
            return super(ImageWidget, self).on_touch_move(touch)
        else:
            return True

#class ImageShuffle(Screen):
class RootWidget(Widget):
    gameStatus = StringProperty('Not Completed')
    myImageList = ['ZERO.JPG', 'ONE.JPG', 'TWO.JPG', 'THREE.JPG', 'FOUR.JPG', 'FIVE.JPG', 'SIX.JPG',
                            'SEVEN.JPG', 'EIGHT.JPG', 'NINE.JPG', 'AARIT.JPG', 'AISHINI.JPG', 'AISHINI2.JPG', 'AISHINI3.JPG',
                   'AMMA.JPG', 'ATTA.JPG','KAVITA.JPG', 'KAVITA2.JPG', 'TATA.JPG', 'YUDI.JPG', 'ANNA.JPG', 'DONALD.JPG',
                   'ELSA.JPG', 'GOOFY.JPG', 'JASMINE.JPG', 'MERMAID.JPG','MICKEY.JPG', 'MINI.JPG', 'MOANA.JPG', 'RUPUNJAL.JPG',
                   'WONDERW.JPG', "aligator.JPG", "bear.JPG", "dog.JPG", "fox.JPG", "hippo.JPG", "kangaroo.JPG",
                            "lion.JPG","monkey.JPG", "squirrel.JPG", "tiger.JPG", "zebra.JPG" ]
    cardPositioned = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.imgList = random.sample(self.myImageList, 8)
        cell_size = int(Window.height/4)
        for i in range(4):
            cw = ImageWidget(imgicon="images/" + self.imgList[i*2+1], setDrag=False, imgalpha=.3, pos=(0, i * cell_size),
                             size=(cell_size, cell_size))
            cw.addImage()
            self.add_widget(cw)
            cw = ImageWidget(imgicon="images/" + self.imgList[i*2], setDrag=False, imgalpha=.3,
                             pos=(Window.width - cell_size, i * cell_size),
                             size=(cell_size, cell_size))
            cw.addImage()
            self.add_widget(cw)
        for i in range(8):
            cw = ImageWidget(imgicon="images/" + self.imgList[i], setDrag = True,
                             pos=(random.randint(cell_size, Window.width - 2*cell_size),
                                  random.randint(cell_size, Window.height - cell_size)),
                             size=(cell_size,cell_size))
            cw.addImage()
            self.add_widget(cw)

    def update(self, dt):

        if self.cardPositioned == 8:
            content = Button(text='Close')
            popup = Popup(title='You Won!!', content=content,
                          size_hint=(None,None), size=(Window.width/4,Window.height/4), auto_dismiss = False )
            content.bind(on_release=self.closeRW)
            content.bind(on_release=popup.dismiss)
            popup.open()

        for child in self.children:
            if child.setDrag:
                for ch in self.children:
                    if child != ch and child.collide_widget(ch) and child.imgicon == ch.imgicon:
                        #print(child.pos, " ", ch.pos)
                        if (child.pos[0] >= ch.pos[0] -25 and (child.pos[0] <= ch.pos[0] + ch.width + 25)) \
                                and (child.pos[1] >= ch.pos[1] -25 and (child.pos[1] <= ch.pos[1] + ch.height + 25)):
                            child.pos = ch.pos
                            child.setDrag = False
                            self.cardPositioned = self.cardPositioned + 1
                            #print(self.cardPositioned, " game ")
            else:
                pass

    def closeRW(self, obj):
        self.gameStatus='Completed'

class ImageShuffle(Screen):
    def on_pre_enter(self, *args):
        if self.rw.gameStatus == 'Completed':
            self.__init__()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rw = RootWidget(gameStatus='Not Completed')
        self.add_widget(self.rw)
        # call update() every second
        #Clock.schedule_interval(self.rw.update, 1.0)
        Clock.schedule_interval(self.update, 1.0)

    def update(self, obj):
        #print("here")
        if self.rw.gameStatus == 'Completed':
            #print('game completed')
            Clock.unschedule(self.update)
            self.rw.clear_widgets()
            self.manager.current = 'optionscreen'
        else:
            self.rw.update(self.rw)


#drag image app done
#Paint app
class MyPaintW(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mypaint = MyPaintWidget()
        box = FloatLayout()
        box.add_widget(self.mypaint)
        box.add_widget(Button(text='clear', on_press=self.clearCanvas, size_hint=(.2,.1), pos=(0,10)))
        box.add_widget(Button(text='close', on_press=self.closeCanvas, size_hint=(.2,.1), pos=(200,10)))
        self.add_widget(box)
    def clearCanvas(self, obj):
        self.mypaint.canvas.clear()

    def closeCanvas(self, obj):
        self.manager.current = "optionscreen"


class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        color = (random.random(),1, 1)
        with self.canvas:
            Color(*color, mode='hsv')
            Ellipse(pos=(touch.x - 1,touch.y - 1), size=(1,1))
            touch.ud['line'] = Line(points=(touch.x,touch.y))
            #print (touch.ud['line'].points)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x,touch.y]

# Main Screen and its methods
class MainScreen(Screen):
    def on_pre_enter(self, *args):
        useroption=self.manager.get_screen('optionscreen').bpressed #get value from previous/game option screen
        # image names/filenames
        self.NumberImageList = ['ZERO.JPG', 'ONE.JPG', 'TWO.JPG', 'THREE.JPG', 'FOUR.JPG', 'FIVE.JPG', 'SIX.JPG',
                                'SEVEN.JPG', 'EIGHT.JPG', 'NINE.JPG']
        self.FamilyImageList = ['AARIT.JPG', 'AISHINI.JPG', 'AISHINI2.JPG', 'AISHINI3.JPG', 'AMMA.JPG', 'ATTA.JPG',
                                'KAVITA.JPG', 'KAVITA2.JPG', 'TATA.JPG', 'YUDI.JPG']
        self.CartoonImageList = ['ANNA.JPG', 'DONALD.JPG', 'ELSA.JPG', 'GOOFY.JPG', 'JASMINE.JPG', 'MERMAID.JPG',
                                 'MICKEY.JPG', 'MINI.JPG', 'MOANA.JPG', 'RUPUNJAL.JPG', 'WONDERW.JPG']
        self.AnimalImageList = ["aligator.JPG", "bear.JPG", "dog.JPG", "fox.JPG", "hippo.JPG", "kangaroo.JPG",
                                "lion.JPG", "monkey.JPG", "squirrel.JPG", "tiger.JPG", "zebra.JPG"]
        if useroption == 'Number Puzzle':
            self.ImageList = self.NumberImageList
        elif useroption == 'Family Puzzle':
            self.ImageList = self.FamilyImageList
        elif useroption == 'Cartoon Puzzle':
            self.ImageList = self.CartoonImageList
        else:
            self.ImageList = self.AnimalImageList


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_layout = GridLayout(cols=2)

        # create button labels
        imgList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        random.shuffle(imgList)
        # global gameList
        self.prevID = 10
        self.uList = ["images/blank.JPG", "images/blank.JPG", "images/blank.JPG", "images/blank.JPG", "images/blank.JPG", "images/blank.JPG" , "images/blank.JPG", "images/blank.JPG"]
        self.gameList = imgList[:4] + imgList[:4]
        random.shuffle(self.gameList)
        self.button = []
        # create buttons with boxlayout for each row
        #h_layout = BoxLayout()
        for row in range(8):
            self.button.append(
                Button(id='id' + str(row), background_normal="images/blank.JPG", font_size='50', disabled=False, on_press=self.on_button_press))
            #self.button[row].background_normal="images/zebra.JPG"
            main_layout.add_widget(self.button[row])
            # add on press event function
            # self.button[row].bind(on_press=self.on_button_press)

            '''if row % 2 != 0:
                # add each row layout to mainlayout
                main_layout.add_widget(h_layout)
                h_layout = BoxLayout()'''
        self.add_widget(main_layout)

    def on_button_press(self, instance):
        currID = int(instance.id[-1]) # button id pressed - 0,1,2..5
        #print(instance.background_normal)
        if instance.background_normal == "images/blank.JPG":
            instance.background_normal = 'images/'+self.ImageList[int(self.gameList[currID])]  # get background
            self.uList[int(currID)] = instance.background_normal  # save pressed text to UserList
            if self.prevID != 10:  # not a first time press
                if self.button[self.prevID].background_normal == instance.background_normal:  # prev and current pressed buttons have same values
                    pass
                else:  # if no match flip the prev button
                    if self.uList.count(self.button[self.prevID].background_normal) < 2:
                        self.button[self.prevID].background_normal = "images/blank.JPG"
                        self.uList[self.prevID] = "images/blank.JPG"
            self.prevID = currID
        else:
            #print(instance.background_normal)
            if self.uList.count(instance.background_normal) < 2:
                instance.background_normal = "images/blank.JPG"
        #print('images/'+self.ImageList[int(self.gameList[currID])])
        if self.uList.count("images/blank.JPG") == 0:
            #for row in range(6):
            #    self.button[row].disabled = True

            b = FloatLayout()

            l=Label(text="You Won!!", color=(0,0,1,1), font_size=150, pos_hint={'x': 0.3, 'y': .6}, size_hint=(.5, .4))
            with l.canvas:
                Color(0, 1, 0, .25)
                Rectangle(pos=self.pos,size=self.size)
            b.add_widget(l)
            b.add_widget(Button(text="Play Again?", font_size=30, pos_hint={'x': 0.4, 'y': .4}, size_hint=(.25, .2),
                                on_press=self.switchscreen))
            b.add_widget(Button(text="Close", font_size=30, pos_hint={'x': 0.4, 'y': .2}, size_hint=(.25, .2),
                                on_press=self.switchscreen))
            self.add_widget(b)

    def switchscreen(self, instance):
        if instance.text == 'Close':
            App.get_running_app().stop()
        else:
            self.__init__()
            self.manager.current = 'optionscreen'

sm = ScreenManager()
class PicMatchGame(App):

    def build(self):
        # create screen manager
        global sm
        sc_login = Optionscreen(name="optionscreen")
        sc_main = MainScreen(name="mainscreen")
        sc_paint= MyPaintW(name="paint")
        sc_imgshuffle = ImageShuffle(name="imgshuffle")

        sm.add_widget(sc_login)
        sm.add_widget(sc_main)
        sm.add_widget(sc_paint)
        sm.add_widget(sc_imgshuffle)
        return sm

if __name__ == '__main__':
    PicMatchGame().run()
