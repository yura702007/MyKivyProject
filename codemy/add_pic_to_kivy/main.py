from kivy.app import App
from kivy.uix.widget import Widget
# from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder
# from kivy.uix.image import Image
from kivy.core.window import Window

Builder.load_file('image.kv')


class MyWidget(Widget):
    pass


class MyApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return MyWidget()


if __name__ == '__main__':
    MyApp().run()
