import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy import Config
Config.set('graphics', 'multisamples', '0')


class SimpleCalculatorApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(multiline=False, readonly=True, halign="right", font_size=55)
        main_layout.add_widget(self.solution)
        #create button labels
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"]
        ]
        #create buttons with boxlayout for each row
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label)
                #add on press event function
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            #add each row layout to mainlayout
            main_layout.add_widget(h_layout)
        #create equal button
        equals_button = Button(text="=")
        equals_button.bind(on_press=self.on_solution)
        #add equal_button to main layout
        main_layout.add_widget(equals_button)

        return main_layout


    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            self.solution.text=""
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                #if operators are pressed symultaneously, dont do anything
                return
            elif current =="" and button_text in self.operators:
                #if first press is operator, dont do anything
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text

        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self,instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution


if __name__ == '__main__':
    SimpleCalculatorApp().run()
