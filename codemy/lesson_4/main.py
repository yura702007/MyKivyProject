from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyWidget(Widget):
    pass


class MyApp(App):
    widget = MyWidget()

    def build(self):
        return self.widget


if __name__ == '__main__':
    MyApp().run()
