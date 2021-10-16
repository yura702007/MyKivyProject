from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_file('switch.kv')


class MyWidget(Widget):
    def switch_active(self, switch_value):
        if switch_value:
            self.ids.my_label.text = 'The Switch is On'
        else:
            self.ids.my_label.text = 'The Switch is Off'

    def on_switch(self):
        if self.ids.my_switch.disabled:
            self.ids.my_switch.disabled = False
        else:
            self.ids.my_switch.disabled = True


class MySomeApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    MySomeApp().run()
