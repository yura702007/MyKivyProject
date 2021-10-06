from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyLabel(Label):
    font_size = 24

    def __init__(self, **kwargs):
        super(MyLabel, self).__init__(**kwargs)
        self.size_hint_x = None
        self.size_hint_y = None
        self.width = 200
        self.height = 50


class Input(TextInput):
    multiline = False

    def __init__(self, **kwargs):
        super(Input, self).__init__(**kwargs)
        self.size_hint_x = None
        self.size_hint_y = None
        self.width = 200
        self.height = 50


class MyButton(Button):
    font_size = 32

    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.size_hint_x = None
        self.width = 440
        self.size_hint_y = None
        self.height = 100


class MyWidgetIn(GridLayout):
    cols = 2
    padding = [20, 20, 20, 20]
    spacing = [10, 10]

    def __init__(self, **kwargs):
        super(MyWidgetIn, self).__init__(**kwargs)
        self.size_hint_x = None
        self.width = 400
        self.size_hint_y = None
        self.height = 100
        self.name = MyLabel(text='Name')
        self.add_widget(self.name)
        self.input_name = (Input())
        self.add_widget(self.input_name)
        self.pizza = MyLabel(text='Pizza')
        self.add_widget(self.pizza)
        self.input_pizza = Input()
        self.add_widget(self.input_pizza)
        self.color = MyLabel(text='Color')
        self.add_widget(self.color)
        self.input_color = Input()
        self.add_widget(self.input_color)


class MyWidgetOut(GridLayout):
    cols = 1
    padding = [40, 40, 40, 40]
    spacing = [20, 20]

    def __init__(self, **kwargs):
        super(MyWidgetOut, self).__init__(**kwargs)
        self.widget_in = MyWidgetIn()
        self.label = Label(
            text='Output',
            font_size=32,
            size_hint_x=None,
            size_hint_y=None,
            width=440,
            height=200
        )
        self.button = MyButton(text='Submit')
        self.add_widget(self.widget_in)
        self.add_widget(self.label)
        self.add_widget(self.button)
        self.button.bind(on_press=self.press)

    def press(self, instance):
        name = self.widget_in.input_name.text
        pizza = self.widget_in.input_pizza.text
        color = self.widget_in.input_color.text
        output = f'My name is {name},\nmy favorite pizza is {pizza}\nand i like {color} color.'
        self.label.text = output
        self.widget_in.input_name.text = ''
        self.widget_in.input_pizza.text = ''
        self.widget_in.input_color.text = ''


class MyApp(App):
    def build(self):
        return MyWidgetOut()


if __name__ == '__main__':
    MyApp().run()
