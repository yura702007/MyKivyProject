from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder
from kivy.core.window import Window

# set app size
Window.size = (500, 700)

Builder.load_file('calculator.kv')


class MyWidget(Widget):
    pass


class MyCalculator(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    MyCalculator().run()
