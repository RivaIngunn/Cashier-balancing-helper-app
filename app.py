import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Layout(GridLayout):
    def __init__(self, **kwargs):
        super(Layout, self).__init__(**kwargs)

        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text =('1000: ')))
        self.thousand = TextInput(multiline = False)
        self.inside.add_widget(self.thousand)


        self.inside.add_widget(Label(text =('500: ')))
        self.five_hundred = TextInput(multiline = False)
        self.inside.add_widget(self.five_hundred)

        self.inside.add_widget(Label(text =('200: ')))
        self.two_hundred = TextInput(multiline = False)
        self.inside.add_widget(self.two_hundred)

        self.inside.add_widget(Label(text =('100: ')))
        self.one_hundred = TextInput(multiline = False)
        self.inside.add_widget(self.one_hundred)

        self.inside.add_widget(Label(text =('50: ')))
        self.fifty = TextInput(multiline = False)
        self.inside.add_widget(self.fifty)

        self.inside.add_widget(Label(text =('20: ')))
        self.twenty = TextInput(multiline = False)
        self.inside.add_widget(self.twenty)

        self.inside.add_widget(Label(text =('10: ')))
        self.ten = TextInput(multiline = False)
        self.inside.add_widget(self.ten)

        self.inside.add_widget(Label(text =('5: ')))
        self.five = TextInput(multiline = False)
        self.inside.add_widget(self.five)

        self.inside.add_widget(Label(text =('1: ')))
        self.one = TextInput(multiline = False)
        self.inside.add_widget(self.one)

        self.add_widget(self.inside)


        self.calculate = Button(text = "Kalkuler", font_size = 40)
        self.calculate.bind(on_press = self.pressed)
        self.add_widget(self.calculate)


    def pressed(self, instance):
        thousand = self.thousand.text
        five_hundred = self.five_hundred.text
        two_hundred = self.two_hundred.text
        one_hundred = self.one_hundred.text
        fifty = self.fifty.text
        twenty = self.twenty.text
        ten = self.ten.text
        five = self.five.text
        one = self.one.text

        print ('thousand', thousand, 'fifty', fifty)

class CashierBalancing(App):
    def build(self):
        return Layout()

if __name__ == "__main__":
    CashierBalancing().run()
