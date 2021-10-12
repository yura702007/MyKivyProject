from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_file('checkbox.kv')


class MyWidget(Widget):
    def checkbox_click(self, instance, value, topping):
        if value:
            self.ids.label_output.text = f'You selected {topping}'


class CheckBoxApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    CheckBoxApp().run()
