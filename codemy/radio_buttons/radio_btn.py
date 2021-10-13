from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_file('radio_btn.kv')


class MyWidget(Widget):
    pass


class ButtonsApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    ButtonsApp().run()
