import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from oppgjor import totalt_i_kassa

class Layout(GridLayout):
    def __init__(self, **kwargs):
        super(Layout, self).__init__(**kwargs)

        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text =('1000: ')))
        self.thousand = TextInput(multiline = False)
        self.inside.add_widget(self.thousand)
        self.thousand.text = '0'


        self.inside.add_widget(Label(text =('500: ')))
        self.five_hundred = TextInput(multiline = False)
        self.inside.add_widget(self.five_hundred)
        self.five_hundred.text = '0'

        self.inside.add_widget(Label(text =('200: ')))
        self.two_hundred = TextInput(multiline = False)
        self.inside.add_widget(self.two_hundred)
        self.two_hundred.text = '0'

        self.inside.add_widget(Label(text =('100: ')))
        self.one_hundred = TextInput(multiline = False)
        self.inside.add_widget(self.one_hundred)
        self.one_hundred.text = '0'

        self.inside.add_widget(Label(text =('50: ')))
        self.fifty = TextInput(multiline = False)
        self.inside.add_widget(self.fifty)
        self.fifty.text = '0'

        self.inside.add_widget(Label(text =('20: ')))
        self.twenty = TextInput(multiline = False)
        self.inside.add_widget(self.twenty)
        self.twenty.text = '0'

        self.inside.add_widget(Label(text =('10: ')))
        self.ten = TextInput(multiline = False)
        self.inside.add_widget(self.ten)
        self.ten.text = '0'


        self.inside.add_widget(Label(text =('5: ')))
        self.five = TextInput(multiline = False)
        self.inside.add_widget(self.five)
        self.five.text = '0'

        self.inside.add_widget(Label(text =('1: ')))
        self.one = TextInput(multiline = False)
        self.inside.add_widget(self.one)
        self.one.text = '0'

        self.add_widget(self.inside)


        self.calculate = Button(text = "Kalkulér", font_size = 40)
        self.calculate.bind(on_press = self.pressed)
        self.add_widget(self.calculate)


    def pressed(self, instance):
        thousand = int(self.thousand.text)
        five_hundred = int(self.five_hundred.text)
        two_hundred = int(self.two_hundred.text)
        one_hundred = int(self.one_hundred.text)
        fifty = int(self.fifty.text)
        twenty = int(self.twenty.text)
        ten = int(self.ten.text)
        five = int(self.five.text)
        one = int(self.one.text)

        value_list, kassa, posen = totalt_i_kassa(thousand, five_hundred, two_hundred, one_hundred, fifty, twenty, ten, five, one)
        self.clear_widgets()
        self.cols = 3

        self.value_title = Label(text = 'Lapp/Mynt')
        self.add_widget(self.value_title)

        self.kassa_title = Label(text = 'Kassa')
        self.add_widget(self.kassa_title)

        self.posen_title = Label(text = 'Posen')
        self.add_widget(self.posen_title)

        for i in value_list:
            self.value = Label(text = str(i))
            self.add_widget(self.value)

            self.kassa = Label(text = str(int(kassa[str(i)]/i)))
            self.add_widget(self.kassa)

            self.posen = Label(text = str(int(posen[str(i)]/i)))
            self.add_widget(self.posen)

        self.sum_title = Label(text = 'Sum')
        self.add_widget(self.sum_title)

        self.sum_kassa = Label(text = str(sum(kassa.values())))
        self.add_widget(self.sum_kassa)

        self.sum_posen = Label(text = str(sum(posen.values())))
        self.add_widget(self.sum_posen)






        #things to fix:
        #   have to write something in all the boxes

class CashierBalancing(App):
    def build(self):
        return Layout()

if __name__ == "__main__":
    CashierBalancing().run()
