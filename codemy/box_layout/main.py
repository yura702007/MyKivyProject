from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder

Builder.load_file('main.kv')


class MyWidget(Widget):
    pass


class MainApp(App):
    widget = MyWidget()

    def build(self):
        return self.widget


if __name__ == '__main__':
    MainApp().run()
