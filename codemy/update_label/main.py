from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder

Builder.load_file('update_label.kv')


class MyWidget(Widget):
    def press(self):
        name = self.ids.name_input.text
        self.ids.name_label.text = f'Hello, {name}!'
        self.ids.name_input.text = ''


class MyApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    MyApp().run()
