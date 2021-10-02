from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyInput(TextInput):
    multiline = False


class MyButton(Button):
    font_size = 42


class MyLabel(Label):
    font_size = 32


class MyGridLayout(GridLayout):
    cols = 2
    padding = [42, 42, 42, 42]
    spacing = [25, 25]


class MyApp(App):
    grid = MyGridLayout()
    name = MyLabel(text='Name: ')
    input_name = MyInput()
    pizza = MyLabel(text='My favorite pizza: ')
    input_pizza = MyInput()
    my_color = MyLabel(text='My favorite color: ')
    input_color = MyInput()
    my_button = MyButton(text='Submit')

    def build(self):
        self.grid.add_widget(self.name)
        self.grid.add_widget(self.input_name)
        self.grid.add_widget(self.pizza)
        self.grid.add_widget(self.input_pizza)
        self.grid.add_widget(self.my_color)
        self.grid.add_widget(self.input_color)
        self.grid.add_widget(self.my_button)
        self.my_button.bind(on_press=self.press)
        return self.grid

    def press(self, instance):
        name = self.input_name.text
        pizza = self.input_pizza.text
        color = self.input_color.text
        with open('file.txt', 'a', encoding='utf8') as file:
            file.write(f'{name}, {pizza}, {color}\n')
        self.input_name.text = ''
        self.input_pizza.text = ''
        self.input_color.text = ''


if __name__ == '__main__':
    MyApp().run()
