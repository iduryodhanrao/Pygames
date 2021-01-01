from kivy.app import App
from kivy.uix.button import Button


class TestApp(App):
   def build(self):
       b=Button(text='Hello')
       return b

if __name__ == '__main__' :
    TestApp().run()