from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder
from kivy.core.window import Window

Builder.load_file('inherit.kv')


class MyWidget(Widget):
    pass


class MyApp(App):
    widget = MyWidget()

    def build(self):
        Window.clearcolor = (0.32, 0.87, 0.61, 1)
        return self.widget


if __name__ == '__main__':
    MyApp().run()
