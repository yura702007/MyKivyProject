from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_file('round_btn.kv')


class MyWidget(Widget):
    pass


class MyApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return MyWidget()


if __name__ == '__main__':
    MyApp().run()
