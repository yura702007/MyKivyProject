from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MyWidget(BoxLayout):
    pass


class MyMenuApp(App):

    def build(self):
        widget = MyWidget()
        return widget


if __name__ == '__main__':
    MyMenuApp().run()
