from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_file('radio_btn.kv')


class MyWidget(Widget):
    def checkbox_click(self, instance, value, topping):
        if value:
            self.ids.label_output.text = f'You selected pizza topping - {topping}'
        else:
            self.ids.label_output.text = ''


class ButtonsApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    ButtonsApp().run()
