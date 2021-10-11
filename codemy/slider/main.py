from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_file('slider.kv')


class MyWidget(Widget):
    pass


class SliderApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    SliderApp().run()
