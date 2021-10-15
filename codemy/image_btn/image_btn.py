from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_file('image_btn.kv')


class MyWidget(Widget):
    def hello_on(self):
        self.ids.my_label.text = 'You pressed the button'
        self.ids.my_image.source = 'on_press.png'

    def hello_off(self):
        self.ids.my_label.text = 'Hello World'
        self.ids.my_image.source = 'press.png'


class MySomeApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    MySomeApp().run()
