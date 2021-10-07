from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty

Builder.load_file('main.kv')


class MyWidget(Widget):
    name = ObjectProperty()
    pizza = ObjectProperty()
    my_color = ObjectProperty()
    output_info = ObjectProperty()

    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        my_color = self.my_color.text
        output = f'My name is {name},\ni like pizza {pizza},\nmy favorite color - {my_color}'
        self.output_info.text = output
        self.name.text = ''
        self.pizza.text = ''
        self.my_color.text = ''


class MainApp(App):
    widget = MyWidget()

    def build(self):
        return self.widget


if __name__ == '__main__':
    MainApp().run()
