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
    pass


class MyApp(App):
    widgets = (
        MyLabel(text='Name:'),
        MyInput(),
        MyLabel(text='My favorite pizza:'),
        MyInput(),
        MyLabel(text='My favorite color:'),
        MyInput()
    )
    padding = [42, 42, 42, 42]
    spacing = [25, 25]
    grid_0 = MyGridLayout(cols=1, padding=padding, spacing=spacing)
    output_label = MyLabel()
    my_button = MyButton(text='Submit')

    def build(self):
        grid_1 = self.make_widget()
        self.grid_0.add_widget(grid_1)
        self.grid_0.add_widget(self.output_label)
        self.grid_0.add_widget(self.my_button)
        self.my_button.bind(on_press=self.press)
        return self.grid_0

    def make_widget(self):
        padding = [20, 20, 20, 20]
        spacing = [10, 10]
        layout = MyGridLayout(cols=2, padding=padding, spacing=spacing)
        for widget in self.widgets:
            layout.add_widget(widget)
        return layout

    def press(self, instance):
        data = self.widgets
        res = f'My name is {data[1].text},\n' \
              f'{data[2].text[:-1].lower()} is a {data[3].text},\n' \
              f'i liked {data[5].text} color'
        self.output_label.text = res


if __name__ == '__main__':
    MyApp().run()
