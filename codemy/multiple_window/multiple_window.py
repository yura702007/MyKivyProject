from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

Builder.load_file('window.kv')


class MyWidget(Widget):
    pass


class MainApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    MainApp().run()
