from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_file('image_btn.kv')


class MyWidget(Widget):
    def hello_on(self):
        self.ids.my_label.text = 'You pressed the button'


class MySomeApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    MySomeApp().run()
