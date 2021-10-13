from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_file('popup.kv')


class MyWidget(Widget):
    pass


# имя класса != имя файл.kv !!!
class SampleApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    SampleApp().run()
